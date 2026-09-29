import config
import random

def registrar_entrada(autos_dentro, placa):
    """Agrega la placa a la lista de autos dentro."""
    autos_dentro.append(placa)


def registrar_salida(autos_dentro, placa):
    """Quita la placa de la lista de autos dentro."""
    autos_dentro.remove(placa)


def espacios_ocupados(autos_dentro):
    """Devuelve la cantidad de espacios ocupados"""
    return len(autos_dentro)


def porcentaje_ocupacion(autos_dentro):
    """Calcula el porcentaje de espacios ocupados"""
    if config.CAPACIDAD_MAX <= 0:
        raise ValueError("La capacidad maxima debe ser mayor que cero")

    return espacios_ocupados(autos_dentro) / config.CAPACIDAD_MAX * 100


def estado_estacionamiento(autos_dentro):
    """Calcula el estado del estacionamiento como disponible, medio ocupado o lleno"""
    porcentaje = porcentaje_ocupacion(autos_dentro)

    if porcentaje >= 100:
        return "lleno"
    if porcentaje >= 50:
        return "medio ocupado"
    return "disponible"


def espacios_libres(autos_dentro):
    """Calcula cuantos espacios quedan libres."""
    libres = config.CAPACIDAD_MAX - espacios_ocupados(autos_dentro)
    return max(libres, 0)

def asignar_espacios(espacios):
    """Busca un espacio libre aleatorio y lo devuelve."""
    
    espaciosLibres = []
    
    for numero in range(1, config.CAPACIDAD_MAX + 1):
        espacio = f"P-{numero:02d}"

        if espacio not in espacios.values():
            espaciosLibres.append(espacio)
        
    if espaciosLibres:
        return random.choice(espaciosLibres)
    return None