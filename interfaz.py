"""Ventana de solo lectura con el mapa y la consola de actividad."""

import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk


def iniciar_interfaz(obtener_resumen, obtener_mensajes):
    ventana = tk.Tk()
    ventana.title("Sistema de Estacionamiento")
    ventana.geometry("1100x720")

    contenedor = tk.Frame(ventana, padx=28, pady=24)
    contenedor.pack(fill="both", expand=True)
    contenedor.grid_columnconfigure(0, weight=3)
    contenedor.grid_columnconfigure(1, weight=2)
    contenedor.grid_rowconfigure(0, weight=1)

    ladoizq = tk.Frame(contenedor, padx=14, pady=10)
    ladoizq.grid(row=0, column=0, sticky="nsew")
    ladoder = tk.Frame(contenedor, padx=14, pady=10)
    ladoder.grid(row=0, column=1, sticky="nsew")

    imagen_path = Path(__file__).resolve().parent / "assets" / "Estacionamiento.jpg"
    imagen = Image.open(imagen_path).resize((700, 650))
    imagen_tk = ImageTk.PhotoImage(imagen)
    canvas = tk.Canvas(ladoizq, width=700, height=650, highlightthickness=0)
    canvas.pack(expand=True)
    canvas.create_image(0, 0, anchor="nw", image=imagen_tk)

    tk.Label(ladoder, text="Consola", font=("Arial", 12, "bold")).pack(anchor="w")
    consola = tk.Text(ladoder, bg="black", fg="white", font=("Consolas", 10),
                      state="disabled", wrap="word", width=36, height=32)
    consola.pack(fill="both", expand=True, pady=(6, 0))

    posiciones = {
        "P-01": (180, 165), "P-02": (270, 165), "P-03": (360, 165),
        "P-04": (450, 165), "P-05": (540, 165), "P-06": (630, 165),
        "P-07": (180, 505), "P-08": (270, 505), "P-09": (360, 505),
        "P-10": (450, 505), "P-11": (540, 505), "P-12": (630, 505),
    }
    etiquetas = {}
    for espacio, (x, y) in posiciones.items():
        rectangulo = canvas.create_rectangle(x - 27, y - 17, x + 27, y + 17,
                                             fill="#55aa77", outline="black")
        texto = canvas.create_text(x, y, text=espacio, fill="white",
                                   font=("Consolas", 9, "bold"))
        etiquetas[espacio] = (rectangulo, texto)

    def actualizar():
        datos = obtener_resumen()
        espacios = datos["espacios"]

        for espacio, (rectangulo, texto) in etiquetas.items():
            placa = next((p for p, asignado in espacios.items()
                          if asignado == espacio), None)
            canvas.itemconfig(rectangulo, fill="#d9534f" if placa else "#55aa77")
            canvas.itemconfig(texto, text=placa if placa else espacio)

        mensajes = obtener_mensajes()
        if mensajes:
            consola.configure(state="normal")
            for mensaje in mensajes:
                consola.insert("end", "> " + mensaje + "\n")
            consola.see("end")
            consola.configure(state="disabled")

        ventana.after(200, actualizar)

    actualizar()
    ventana.mainloop()
