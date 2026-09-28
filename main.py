"""Coordina la lógica del estacionamiento y abre su vista gráfica."""

import random
import threading
from queue import Empty, Queue

import config
import eventos
import parking


autos_dentro = []
historia = eventos.inicializar_historial()
espacios = {}
mensajes = Queue()
bloqueo = threading.Lock()


def registrar_entrada():
    """Registra una entrada usando las funciones de parking y eventos."""
    with bloqueo:
        placa = eventos.generar_placa()
        while placa in autos_dentro:
            placa = eventos.generar_placa()

        espacio = parking.asignar_espacios(espacios)
        if espacio is None:
            return None, None

        parking.registrar_entrada(autos_dentro, placa)
        espacios[placa] = espacio
        evento = eventos.evento_entrada(placa)
        eventos.agregar_a_historial(historia, placa, evento)
        return placa, espacio


def registrar_salida():
    """Retira un auto que esté dentro y libera su espacio."""
    with bloqueo:
        if not autos_dentro:
            return None, None

        placa = random.choice(autos_dentro)
        espacio = espacios.pop(placa)
        parking.registrar_salida(autos_dentro, placa)
        evento = eventos.evento_salida(placa)
        eventos.agregar_a_historial(historia, placa, evento)
        return placa, espacio


def obtener_resumen():
    """Prepara una copia del estado para que la interfaz solo lo visualice."""
    with bloqueo:
        return {
            "autos": list(autos_dentro),
            "espacios": dict(espacios),
            "libres": parking.espacios_libres(autos_dentro),
            "ocupacion": parking.porcentaje_ocupacion(autos_dentro),
            "estado": parking.estado_estacionamiento(autos_dentro),
            "capacidad": config.CAPACIDAD_MAX,
        }


def obtener_mensajes():
    """Entrega los mensajes pendientes a la consola gráfica."""
    pendientes = []
    while True:
        try:
            pendientes.append(mensajes.get_nowait())
        except Empty:
            return pendientes


def imprimir(mensaje):
    """Muestra el mensaje en la consola de texto y en la ventana."""
    print(mensaje, flush=True)
    mensajes.put(mensaje)


def pedir_entero(pregunta):
    mensajes.put(pregunta)
    respuesta = input(pregunta)
    mensajes.put(respuesta)
    return int(respuesta)


def ejecutar_consola():
    """Mantiene el flujo original de preguntas y operaciones en consola."""
    while True:
        try:
            entran = pedir_entero("Cuantos autos entran?")
            salen = pedir_entero("Cuantos autos salen?")
        except EOFError:
            return

        contador = 0
        while contador < entran:
            placa, espacio = registrar_entrada()
            if espacio is None:
                imprimir("No hay espacios disponibles")
                break
            imprimir("Vehiculo entrando...")
            imprimir(f"Placa: {placa}")
            imprimir(f"Espacio asignado: {espacio}")
            contador += 1

        contador = 0
        while contador < salen:
            placa, espacio = registrar_salida()
            if placa is None:
                imprimir("No hay autos para sacar")
            else:
                imprimir("Vehiculo saliendo...")
                imprimir(f"Placa: {placa}")
                imprimir(f"Espacio liberado: {espacio}")
            contador += 1

        datos = obtener_resumen()
        imprimir(f"Autos dentro: {datos['autos']}")
        imprimir(f"Espacios libres: {datos['libres']}")
        imprimir(f"Porcentaje de ocupacion: {datos['ocupacion']:.1f}%")
        imprimir(f"Estado: {datos['estado']}")

        try:
            mensajes.put("otro ciclo? s n")
            continuar = input("otro ciclo? s n")
            mensajes.put(continuar)
        except EOFError:
            continuar = "n"
        if continuar != "s":
            break

    with bloqueo:
        imprimir(f"Historial: {historia}")


def iniciar():
    """Ejecuta la consola en segundo plano y Tkinter en el hilo principal."""
    import interfaz

    mensajes.put("Sistema iniciado. Usa la consola para registrar entradas y salidas.")
    hilo_consola = threading.Thread(target=ejecutar_consola, daemon=True)
    hilo_consola.start()
    interfaz.iniciar_interfaz(obtener_resumen, obtener_mensajes)


if __name__ == "__main__":
    iniciar()
