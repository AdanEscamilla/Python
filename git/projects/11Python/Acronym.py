palabras = "a ante bajo contra de desde durante en entre lo la li lu le sin sobre tras mediante hasta hacia para por según traso una uno unos unas y e ni que o u pero"
palabras = palabras.split()

frase = input("Ingrese una frase: ")
frase = frase.split()
siglas = []

for palabra in frase :
    if palabra not in palabras :
        siglas.append(palabra[0])

siglas = "".join(siglas)
siglas = siglas.upper()
print("Tu acrónimo es: "+ siglas)