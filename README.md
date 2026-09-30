# Parcial 1

**Grupo:** 6

## Integrantes

- Alexander Castroverde
- Juan García
- Arles López
- Gloria Moreno
- Luis Moreno

## Descripción

Se desea implementar un sistema de parqueo inteligente para monitorear la ocupación de los
estacionamientos en un centro comercial. El equipo debe simular en Python cómo funcionaría el
sistema. Se deben generar datos simulados y procesarlos con Python.

Funcionalidades principales:

- Constantes de configuración (capacidad máxima y tarifa por hora).
- Registro de entradas y salidas de autos en cada ciclo de simulación.
- Cálculo del porcentaje de ocupación y del estado del parqueo: **disponible**, **medio ocupado** o **lleno**.
- Cantidad de espacios libres.
- Lista de las placas de los autos que están dentro en un momento dado.
- Manejo de errores ante valores inválidos.
- Cada evento se guarda como una tupla `(placa, hora, tarifa)`.
- Un diccionario que guarda el historial de eventos de cada placa.

