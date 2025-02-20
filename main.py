import random

def russianRoulete(a,b):
        a = random.randint(1,5)
        b = random.randint(1,5)

        if a == b:
            print("-"*7)
            print("|Moriste|")
            print("-"*7)
        else:
            print("-"*74)
            print(f" |  Casi!! la bala estaba en el cartucho {b} y disparaste el cartucho {a}  | ")
            print("-"*74)
a=0
b=0
#Historial
story = []
#Menu

while(True):
    print("+" + "-"*12 + "+")
    print("| BIENVENIDO |")
    print("+" + "-"*12 + "+")
    print("Este es el juego de la ruleta rusa, ganas si vives, pierdes si mueres... \n")
    print("O si solo quieres ver el historial pon 1 \n")
    response = input("Te atreves a jugar? ")

    if response == "Si":
        russianRoulete(a,b)
        response2 = input("Quieres seguir jugando? ")
        if response2 == "si":
            print("OK")
        else:
            break
    else:
        break

    


    