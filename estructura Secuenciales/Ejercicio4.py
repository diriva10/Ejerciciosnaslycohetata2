#Calcular el área total de un terreno en metros sabiendo que esta fue reducida en un 10%, y posteriormente, le fue adicionado un 50% con relación al área después de la reducción.

AreaActual=float(input("Escriba el area de un terreno:"))

AreaReducida=AreaActual*0.9

AreaAdicion=AreaReducida*1.5

print(f"El area Final es:{AreaAdicion}")