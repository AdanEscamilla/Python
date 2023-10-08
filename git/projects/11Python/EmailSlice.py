domain = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com"]

email = input("Ingrea tu correo electronico: ").strip()

usuario = email[:email.index('@')]

dominio = email[email.index('@')+1:]

for correo in domain :
    if correo == dominio and dominio == "gmail.com" :
        print("Veo que tu correo esta registrado en Google.\nEso es genial")
        break
    elif correo == dominio and dominio == "outlook.com" :
        print("Veo que tu correo esta registrado en Microsoft.\nEso es genial")
        break
    elif correo == dominio and dominio == "hotmail.com" :
        print("Veo que tu correo esta registrado en Microsoft.\nEso es genial")
        break
    elif correo == dominio and dominio == "yahoo.com" :
        print("Veo que tu correo esta registrado en Yahoo.\nEso es genial")
        break
    else :
        print("Veo que tu correo es uno propio.\nEso es genial")
        break

resultado = "Tu nombre de usuario es {}\nTu nombre de dominio es {}".format(usuario, dominio)

print(resultado)