import random
import eventos
import parking


autos_dentro = []
historia =  eventos.inicializar_historial()

while True:
    entran = int(input("Cuantos autos entran? "))
    salen = int(input("Cuantos autos salen? "))

    contador = 0
    while contador < entran:
        placa = eventos.generar_placa()
        parking.registrar_entrada(autos_dentro, placa)
        evento = eventos.evento_entrada(placa)
        eventos.agregar_a_historial(historia, placa, evento)
        contador = contador + 1

    contador = 0
    while contador < salen:
        if autos_dentro:
            placa = random.choice(autos_dentro)
            parking.registrar_salida(autos_dentro, placa)
            evento = eventos.evento_salida(placa)
            eventos.agregar_a_historial(historia, placa, evento)
        else:
            print("No hay autos para sacar")
        contador = contador + 1

    print("Autos dentro:", autos_dentro)

    if input("otro ciclo? s n") != "s":
        break

print("Historial:", historia)
