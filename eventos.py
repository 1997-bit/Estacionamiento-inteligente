import config
import datetime
import random


def generar_placa():
    """Genera una placa aleatoria para simulación.
    Formato panameño: puede ser dos letras + 4 numeros O todas numericas."""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    # Elegir aleatoriamente el formato: 2 letras + 4 numeros O 6 numeros
    formato = random.choice(["letras_numeros", "numeros_puros"])
    if formato == "letras_numeros":
        # Dos letras seguida de 4 numeros
        parte_letras = "".join(random.choice(letras) for _ in range(2))
        parte_numeros = "".join(random.choice(nums) for _ in range(4))
        placa = parte_letras + parte_numeros
    else:
        # Todas numericas (6 digitos)
        placa = "".join(random.choice(nums) for _ in range(6))
    return placa


def evento_entrada(placa):
    """Crea la tupla (placa, hora de entrada, tarifa)."""
    return (placa, datetime.datetime.now(), config.TARIFA_HORA)


def evento_salida(placa):
    """Crea la tupla (placa, hora de salida, tarifa)."""
    return (placa, datetime.datetime.now(), config.TARIFA_HORA)


def inicializar_historial():
    """Inicializa el diccionario de historial de placas"""
    return {}


def agregar_a_historial(historial, placa, evento):
    """Agrega un evento al historial de una placa"""
    if placa not in historial:
        historial[placa] = []
    historial[placa].append(evento)
    return historial
