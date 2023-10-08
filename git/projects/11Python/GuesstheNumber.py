import random

numero = random.randrange(1,50)
jugador = int(input("Adivine un numero entre el 1 al 50: "))
intentos = 1
jugar = False

while jugador != numero :
    if jugador > 50 :
        print("Adivinaste un numero fuera del rango. Intenta otra vez")
        jugador = int(input("\nAdivine un numero entre el 1 al 50: "))
    elif jugador < numero :
        print("Necesitas adivinar un numero mas alto. Intenta otra vez")
        jugador = int(input("\nAdivine un numero entre el 1 al 50: "))
        intentos+=1
    else :
        print("Necesitas adivinar un numero mas bajo. Intenta otra vez")
        jugador = int(input("\nAdivine un numero entre el 1 al 50: "))
        intentos+=1
print("Adivinaste el numero correcto. !Felicidades!. (tu numero de intentos fue "+ format(str(intentos))+")")


