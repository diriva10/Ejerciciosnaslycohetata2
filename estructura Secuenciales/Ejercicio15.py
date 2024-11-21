'''El sistema de liquidación que hacen los conductores de buses y los colectivos a las
diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro
al terminarlo . La diferencia de estos dos números determina el numero de pasajeros
transportados en el día. Realizar un algoritmo que permita leer estos dos números y el
valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y
el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes
del dinero mientras el conductor recibe el resto.'''

numeroInicial=int(input("Ingrese el Numero inicial de la registradora:"))
numeroFinal=int(input("Ingrese el Numero Final de la registradora:"))
precioPasaje=float(input("Digite el precio del pasaje:"))

totalPasajeros=numeroInicial-numeroFinal

valorTotal=totalPasajeros*precioPasaje
valorConductor=valorTotal/4
valorEmpresa=valorTotal-valorConductor

print(f"Total pasajeros:{totalPasajeros}")
print(f"Valor liquidado al conductor:{valorConductor}")
print(f"Valor liquidado a la empresa:{valorEmpresa}")


