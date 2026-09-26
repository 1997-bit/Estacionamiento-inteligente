import config


def validar_lista_autos(autos_dentro):
    """Valida que autos_dentro sea una lista"""
    if not isinstance(autos_dentro, list):
        raise ValueError("autos_dentro debe ser una lista")


def registrar_entrada(autos_dentro, placa):
    """Registra un auto y devuelve la lista actualizada"""
    validar_lista_autos(autos_dentro)

    if not isinstance(placa, str) or not placa.strip():
        raise ValueError("La placa debe ser un texto no vacio")

    placa = placa.strip().upper()

    if placa in autos_dentro:
        raise ValueError("El auto ya esta dentro del estacionamiento")

    if espacios_ocupados(autos_dentro) >= config.CAPACIDAD_MAX:
        raise ValueError("El estacionamiento esta lleno")

    autos_dentro.append(placa)
    return autos_dentro


def registrar_salida(autos_dentro, placa):
    """Retira un auto y devuelve la lista actualizada"""
    validar_lista_autos(autos_dentro)

    if not isinstance(placa, str) or not placa.strip():
        raise ValueError("La placa debe ser un texto no vacio")

    placa = placa.strip().upper()

    if placa not in autos_dentro:
        raise ValueError("El auto no se encuentra en el estacionamiento.")

    autos_dentro.remove(placa)
    return autos_dentro


def espacios_ocupados(autos_dentro):
    """Devuelve la cantidad de espacios ocupados"""
    validar_lista_autos(autos_dentro)
    return len(autos_dentro)


def porcentaje_ocupacion(autos_dentro):
    """Calcula el porcentaje de espacios ocupados"""
    validar_lista_autos(autos_dentro)

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
    validar_lista_autos(autos_dentro)

    libres = config.CAPACIDAD_MAX - espacios_ocupados(autos_dentro)
    return max(libres, 0)
