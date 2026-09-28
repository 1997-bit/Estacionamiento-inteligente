# Estacionamiento inteligente

Proyecto de simulación para el Parcial #1 de Desarrollo de Software 8.

## Integrantes

- [Escribir nombre de cada integrante]

## Número de grupo

- [Escribir número de grupo]

## Requisitos

- Python 3
- Pillow (`python -m pip install Pillow`)
- Tkinter (incluido en la mayoría de las instalaciones de Python para escritorio)

## Ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
python main.py
```

Se abrirá la interfaz gráfica con el mapa, los espacios ocupados y libres, los vehículos dentro y la consola de actividad.

## Prueba

1. Desde la carpeta del proyecto, ejecuta:

   ```bash
   python main.py
   ```

2. Se abrir? la ventana gr?fica con el mapa del estacionamiento, los 12 espacios, las matr?culas en los espacios ocupados y la consola gr?fica de actividad. Los espacios libres se muestran como P-01 hasta P-12.

3. Registra entradas y salidas escribiendo en la consola de Python. Por ejemplo, para ingresar tres autos y no retirar ninguno:

   ```text
   Cuantos autos entran? 3
   Cuantos autos salen? 0
   ```

   El programa genera autom?ticamente las matr?culas y asigna a cada veh?culo un espacio disponible aleatorio. La consola muestra el veh?culo que entra, su placa, el espacio asignado, los veh?culos dentro, los espacios libres, el porcentaje de ocupaci?n y el estado del estacionamiento.

4. Para retirar un veh?culo, por ejemplo:

   ```text
   Cuantos autos entran? 0
   Cuantos autos salen? 1
   ```

   El programa selecciona un veh?culo que est? dentro, libera su espacio y muestra:

   ```text
   Vehiculo saliendo...
   Placa: XXXXX
   Espacio liberado: P-XX
   ```

5. La interfaz gr?fica se actualiza despu?s de cada operaci?n y el historial se mantiene durante la ejecuci?n.
