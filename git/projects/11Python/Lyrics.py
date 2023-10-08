jugar = True

while (jugar == True) :

    print("Bienvenido, por favor selecciona cualquiera del top 10 canciones para ver su letra\n")

    print("1. 506 de Morat\n2. Azul de Zoé\n3. Level of Concern de Twenty One Pilots\n4. R U Mine? de Artic Monkeys\n5. Somebody Else de The 1975\n6. Te lo Advertí de Los Mesoneros\n7. The Hype de Twenty One Pilots\n8. Those Eyes de New West\n9. ..To be Loved de Papa Roach\n10. Treat You Better de Shawn Mendes\n")

    song=int(input("Su opción: "))

    if song == 1 :
        print("\n-------- 506 de Morat --------\n")
        with open('506.txt', 'r') as file :
            print(file.read())
    elif song == 2 :
        print("\n-------- Azul de Zoé --------\n")
        with open('Azul.txt', 'r') as file :
            print(file.read())
    elif song == 3 :
        print("\n-------- Level of Concern de Twenty One Pilots --------\n")
        with open('LevelOfConcern.txt', 'r') as file :
            print(file.read())
    elif song == 4 :
        print("\n-------- R U Mine? de Artic Monkeys --------\n")
        with open('RUMine.txt', 'r') as file :
            print(file.read())
    elif song == 5 :
        print("\n-------- Somebody Else de The 1975 --------\n")
        with open('SomebodyElse.txt', 'r') as file :
            print(file.read())
    elif song == 6 :
        print("\n-------- Te lo Advertí de Los Mesoneros --------\n")
        with open('TeLoAvertí.txt', 'r') as file :
            print(file.read())
    elif song == 7 :
        print("\n-------- The Hype de Twenty One Pilots --------\n")
        with open('TheHype.txt', 'r') as file :
            print(file.read())
    elif song == 8 :
        print("\n-------- Those Eyes de New West --------\n")
        with open('ThoseEyes.txt', 'r') as file :
            print(file.read())
    elif song == 9 :
        print("\n-------- ..To be Loved de Papa Roach --------\n")
        with open('TobeLoved.txt', 'r') as file :
            print(file.read())
    elif song == 10 :
        print("\n-------- Treat You Better de Shawn Mendes --------\n")
        with open('TreatYouBetter.txt', 'r') as file :
            print(file.read())
    else : 
        print("No escogio ninguno")
    
    decision = input("\nPresione '*' si quiere escuchar otra canción. Si no es así presione cualquier otra tecla para salir.")
    if decision == '*' :
        jugar = True
    else :
        jugar = False
