import random

def russianRoulete(a,b):
        a = random.randint(1,5)
        b = random.randint(1,5)

        if a == b:
              print("Moriste")
        else:
             print(f"Pura suerte, la bala estaba en el cartucho {b} y disparaste el cartucho {a} \n")
a=0
b=0
#Historial
story = []
#Menu

while(True):
    print("Bienvenidoo \n")
    print("Este es el juego de la ruleta rusa, ganas si vives, pierdes si mueres... \n")
    print("O si solo quieres ver el historial pon 1 \n")
    response = (input("Te atreves a jugar? "))

    if response == "Si":
        russianRoulete(a,b)
    else:
        break

    


    