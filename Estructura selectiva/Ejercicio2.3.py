encuentro1=float(input("Digite el primer gol del encuentro:"))
encuentro2=float(input("Digite el segundo gol del encuentro:"))
encuentro3=float(input("Digite el tercer gol del encuentro:"))
encuentro4=float(input("Digite el cuarto gol del encuentro:"))

total=encuentro1+encuentro2+encuentro3+encuentro4

if total>10:
    resultado=total/4
    print(f"El promedio de goles del jugador es:{resultado}")
else:
    print("No se puede determinar el promedio")