
import threading

import ayuda
import interfaz


def ejecutar_consola():
    """Mantiene el flujo original de preguntas y operaciones en consola."""
    while True:
        entran = ayuda.pedir_entero("Cuantos autos entran? ")
        salen = ayuda.pedir_entero("Cuantos autos salen? ")

        contador = 0
        while contador < entran:
            placa, espacio = ayuda.registrar_entrada()
            if espacio is None:
                ayuda.imprimir("No hay espacios disponibles")
                break
            ayuda.imprimir("Vehiculo entrando...")
            ayuda.imprimir(f"Placa: {placa}")
            ayuda.imprimir(f"Espacio asignado: {espacio}")
            contador += 1

        contador = 0
        while contador < salen:
            placa, espacio = ayuda.registrar_salida()
            if placa is None:
                ayuda.imprimir("No hay autos para sacar")
                break
            else:
                ayuda.imprimir("Vehiculo saliendo...")
                ayuda.imprimir(f"Placa: {placa}")
                ayuda.imprimir(f"Espacio liberado: {espacio}")
            contador += 1

        datos = ayuda.obtener_resumen()
        ayuda.imprimir(f"Autos dentro: {datos['autos']}")
        ayuda.imprimir(f"Espacios libres: {datos['libres']}")
        ayuda.imprimir(f"Porcentaje de ocupacion: {datos['ocupacion']:.1f}%")
        ayuda.imprimir(f"Estado: {datos['estado']}")

        ayuda.mensajes.put("otro ciclo? s n ")
        continuar = input("otro ciclo? s n ").lower()
        ayuda.mensajes.put(continuar)
        if continuar != "s":
            break

    ayuda.imprimir_historial()


def iniciar():
    """Ejecuta la consola en segundo plano y Tkinter en el hilo principal."""
    ayuda.mensajes.put("Sistema iniciado. Usa la consola para registrar entradas y salidas.")
    hilo_consola = threading.Thread(target=ejecutar_consola, daemon=True)
    hilo_consola.start()
    interfaz.iniciar_interfaz(ayuda.obtener_resumen, ayuda.obtener_mensajes)


if __name__ == "__main__":
    iniciar()
