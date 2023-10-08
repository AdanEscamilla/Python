recibo = float(input("¿Cúanto es del recibo? "))

propina18 = round(recibo * 0.18, 2)
propina20 = round(recibo * 0.20, 2)
propina25 = round(recibo * 0.25, 2)
total18 = round(propina18 + recibo, 2)
total20 = round(propina20 + recibo, 2)
total25 = round(propina25 + recibo, 2)

personas = int(input("¿Cúantas personas pagaran? "))

personas18 = round(total18 / personas, 2)
personas20 = round(total20 / personas, 2)
personas25 = round(total25 / personas, 2)

print("El 18% de la propina es " + format(str(propina18)) + ", el total seria " + format(str(total18)) + ". Si se separa equitativamente cada quien pagaria " + format(str(personas18)))
print("El 20% de la propina es " + format(str(propina20)) + ", el total seria " + format(str(total20)) + ". Si se separa equitativamente cada quien pagaria " + format(str(personas20)))
print("El 25% de la propina es " + format(str(propina25)) + ", el total seria " + format(str(total25)) + ". Si se separa equitativamente cada quien pagaria " + format(str(personas25)))