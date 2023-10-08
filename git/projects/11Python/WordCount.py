frase = input("¿Qué es lo que tiene en mente? ")
palabras = frase.split()
contador = 0
for i in palabras :
    contador+=1

print("Oh, genial me contaste lo que piensas en " + format(str(contador)) + " palabras")