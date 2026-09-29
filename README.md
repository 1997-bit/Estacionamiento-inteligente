# Parcial 1 - Estacionamiento Inteligente

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


## Instrucciones para ejecutar

1. Descargar el proyecto y abrir una terminal en la carpeta `Estacionamiento-inteligente`.
2. Ejecutar:

```bash
   python main.py
```

3. En cada ciclo de simulación el programa pedirá:
   - Cuántos autos **entran**.
   - Cuántos autos **salen** (se eligen al azar entre los autos que están dentro).
4. Al terminar cada ciclo se muestran los autos que están dentro. Luego el programa pregunta si se desea otro ciclo (`s` para continuar, cualquier otra tecla para terminar).
5. Al finalizar se muestra el historial de eventos por placa.

## Estructura del proyecto

```
Estacionamiento-inteligente/
├── main.py        # Programa principal y ciclo de simulación
├── config.py      # Constantes (CAPACIDAD_MAX, TARIFA_HORA)
├── parking.py     # Lógica del parqueo: entradas, salidas, ocupación, estado y espacios libres
├── eventos.py     # Generación de placas, eventos (tuplas) e historial por placa
├── docs/
│   ├── enunciado.md
│   └── arquitectura.md
└── README.md
```

## Configuración

Los valores se pueden modificar en `config.py`:

| Constante | Valor por defecto | Descripción |
|-----------|-------------------|-------------|
| `CAPACIDAD_MAX` | 20 | Capacidad máxima del estacionamiento |
| `TARIFA_HORA` | 1.20 | Tarifa por hora (en dólares) |

## Estados del parqueo

| Ocupación | Estado |
|-----------|--------|
| Menos de 50 % | Disponible |
| Entre 50 % y 99 % | Medio ocupado |
| 100 % | Lleno |
