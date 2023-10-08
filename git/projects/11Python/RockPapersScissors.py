from random import randint

opcion = ["piedra", "papel", "tijeras"]
def main() :
    compu = opcion[randint(0,2)]

    print("Bienvenido al juego de Piedra, Papel y Tijeras")
    jugador = input("¿Cúal es su opción? ").lower()
    print("Opción de la computadora: "+ compu)

    if jugador == compu :
        print("Empate")
    elif jugador == "piedra" and compu == "papel" : 
        print("Computadora gana")
    elif jugador == "piedra" and compu == "tijeras" :
        print("Jugador gana")
    elif jugador == "papel" and compu == "piedra" :
        print("Jugador gana")
    elif jugador == "papel" and compu == "tijeras" :
        print("Computadora gana")
    elif jugador == "tijeras" and compu == "piedra" : 
        print("Computadora gana")
    elif jugador == "tijeras" and compu == "papel" :
        print("Jugador gana")
    main()

main()