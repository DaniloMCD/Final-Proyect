import random

def russianRoulete(a, b, historial):
    a = random.randint(1, 5)
    b = random.randint(1, 5)

    if a == b:
        print("-" * 10)
        print("|Moriste|")
        print("-" * 10)
        historial.append("Perdiste")
    else:
        print("-" * 74)
        print(f" |  Casi!! la bala estaba en el cartucho {b} y disparaste el cartucho {a}  | ")
        print("-" * 74)
        historial.append("Ganaste")

a = 0
b = 0
historial = []

# Menu
while True:
    print("+" + "-" * 12 + "+")
    print("| BIENVENIDO |")
    print("+" + "-" * 12 + "+")
    print("Este es el juego de la ruleta rusa, ganas si vives, pierdes si mueres... \n")
    print("O si solo quieres ver el historial pon 1 \n")
    response = input("Te atreves a jugar? ")

    if response.lower() == "si":
        print("BAMM \n")
        russianRoulete(a, b, historial)
        response2 = input("Quieres seguir jugando? ")
        if response2.lower() != "si":
            break
    elif response == "1":
        print("Historial de partidas:")
        for i, resultado in enumerate(historial, start=1):
            print(f"Partida {i}: {resultado}")
    else:
        print("Pff cobarde")
        break

    


    