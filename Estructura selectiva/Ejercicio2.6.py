salario=float(input("Ingrese la cantida de tu salario:"))

if salario<=50000:
    print("Puedes comprar una Camara web")
elif salario>=50000 and salario<= 200000:
    print("Puedes comprar un Subwoofer")
elif salario>=200000 and salario<= 500000:
    print("Puedes comprar un DD externo")
elif salario>=500000 and salario<= 1000000:
    print("Puedes comprar una impresora multifuncional")
elif salario>=1000000:
    print("Puedes comprar un Proyector")
    
