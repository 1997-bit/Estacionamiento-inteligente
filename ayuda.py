"""Estado del estacionamiento y funciones de ayuda que usa main.py."""

import random
import threading
from queue import Queue

import eventos
import parking


autos_dentro = []
historia = {}
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
        }


def obtener_mensajes():
    """Entrega los mensajes pendientes a la consola gráfica."""
    pendientes = []
    while not mensajes.empty():
        pendientes.append(mensajes.get())
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


def formatear_historial(historial):
    """Devuelve el historial agrupado por placa y ordenado cronológicamente."""
    if not historial:
        return "Historial vacío: no se registraron eventos."

    lineas = ["Historial de movimientos:"]
    for placa, eventos_placa in historial.items():
        lineas.append(f"Placa {placa}:")
        for indice, (_, hora, tarifa) in enumerate(eventos_placa):
            tipo = "Entrada" if indice % 2 == 0 else "Salida"
            momento = hora.strftime("%d/%m/%Y %H:%M:%S")
            lineas.append(f"  - {tipo}: {momento} | Tarifa: ${tarifa:.2f}")
    return "\n".join(lineas)


def imprimir_historial():
    """Muestra el historial completo al terminar la simulación."""
    with bloqueo:
        imprimir(formatear_historial(historia))
