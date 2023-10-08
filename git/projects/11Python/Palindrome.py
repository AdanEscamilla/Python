def convertInputString():
    Input = input("\nPor favor ingrese una palabra frase, o sentencia \npara checar si es palindromo: ") 
    rawString = Input.lower() 
    rawList = list(rawString) 
    return rawList

def quitarAnalfabeticos(dirtyList): 
    analfabeto = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for letra in analfabeto: 
        if letra in dirtyList: 
            dirtyList.remove(letra) 
            return quitarAnalfabeticos(dirtyList)
    return dirtyList 

def correrPalindromo(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "El texto que ingresaste es palindromo!" 
    else: 
        return "El texto que ingresaste no es palindromo." 

def main(): 
    print("\nChecador de palindromos") 
    originalList = convertInputString()  
    originalList = quitarAnalfabeticos(originalList) 
    palindromeCheck = correrPalindromo(originalList)
    print(palindromeCheck)

main() 