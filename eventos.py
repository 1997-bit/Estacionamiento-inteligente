import config
import datetime
import random
import parking


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


def evento_entrada(placa, tarifa=None):
    """Crea un tupla de evento de entrada (placa, hora, tarifa)"""
    hora = datetime.datetime.now()
    if tarifa is None:
        tarifa = config.TARIFA_HORA
    return (placa, hora, tarifa)


def evento_salida(placa, hora_salida=None, tarifa=None):
    """Crea un tupla de evento de salida (placa, hora, tarifa)"""
    if hora_salida is None:
        hora_salida = datetime.datetime.now()
    if tarifa is None:
        tarifa = config.TARIFA_HORA
    return (placa, hora_salida, tarifa)


def inicializar_historial():
    """Inicializa el diccionario de historial de placas"""
    return {}


def agregar_a_historial(historial, placa, evento):
    """Agrega un evento al historial de una placa"""
    if placa not in historial:
        historial[placa] = []
    historial[placa].append(evento)
    return historial


def obtener_historial(historial, placa):
    """Obtiene el historial de eventos de una placa"""
    return historial.get(placa, [])


def simular_entrada(autos_dentro, historial, tarifa=None):
    """Registra una entrada simulada y devuelve placa y evento."""
    placa = generar_placa()
    while placa in autos_dentro:
        placa = generar_placa()
    evento = evento_entrada(placa, tarifa)
    parking.registrar_entrada(autos_dentro, placa)
    agregar_a_historial(historial, placa, evento)
    return autos_dentro, historial, placa, evento


def simular_salida(autos_dentro, historial, tarifa=None):
    """Retira un auto que esté dentro y guarda el evento de salida."""
    if not autos_dentro:
        return autos_dentro, historial, None, None
    placa = random.choice(autos_dentro)
    return registrar_salida(autos_dentro, historial, placa, tarifa)


def registrar_salida(autos_dentro, historial, placa, tarifa=None):
    """Registra la salida de una placa específica que esté dentro."""
    placa = placa.strip().upper() if isinstance(placa, str) else placa
    evento_sal = evento_salida(placa, tarifa=tarifa)
    parking.registrar_salida(autos_dentro, placa)
    agregar_a_historial(historial, placa, evento_sal)
    return autos_dentro, historial, placa, evento_sal


def mostrar_historial_placa(historial, placa):
    """Muestra el historial formateado de una placa"""
    eventos = obtener_historial(historial, placa)
    if not eventos:
        return f"No hay eventos para la placa {placa}"
    resultado = f"Historial de {placa}:\n"
    for i, (p, h, t) in enumerate(eventos, 1):
        resultado += f"  {i}. Hora: {h.strftime('%H:%M:%S')} | Tarifa: ${t:.2f} | {'Entrada' if any(e[0] == p and e[1] < h for e in eventos) else 'Salida'}\n"
    return resultado.strip()
