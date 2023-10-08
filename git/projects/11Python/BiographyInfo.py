name = input("Ingrese su nombre: ")
date = input("Ingrese una fecha: ")
direccion = input("Ingrese su dirección: ")
goals = input("Ingrese una meta personal: ")

if name.isalpha() :
    print("El valor del nombre debe ser una palabra")
else :
    print("Name: "+ name)

if date.isalnum() :
    print("El valor de la fecha solo permite valores alfanumericos")
else :
    print("Date: "+ date)

if direccion.isalnum() :
    print("El valor de la dirección solo permite valores alfanumericos")
else :
    print("Address: "+ direccion)

if goals.isalnum() :
    print("El valor de la meta solo permite valores alfanumericos")
else :
    print("Goal: "+ goals)

