#Un atleta tiene la costumbre de medir el tiempo(en minutos) y la distancia (en metros)
#durante sus tres días de entrenamiento. Al final de la semana quiere saber el total de
#tiempo que duro el entrenamiento , la distancia recorrida, y el promedio del tiempo y la
#distancia recorrida.

dia1=float(input("Ingrese el Tiempo del Dia 1:"))
distancia1=float(input("Ingrese la Distacia que recorrio del Dia 1:"))

dia2=float(input("Ingrese el Tiempo del Dia 2:"))
distancia2=float(input("Ingrese la Distacia que recorrio del Dia 2:"))

dia3=float(input("Ingrese el Tiempo del Dia 3:"))
distancia3=float(input("Ingrese la Distacia que recorrio del Dia 3:"))

totalTiempo=dia1+dia2+dia3
totalDistacia=distancia1+distancia2+distancia3

promedioTiempo=totalTiempo/3
promedioDistancia=totalDistacia/3

print(f"El tiempo total es de: {totalTiempo}Minutos ")
print(f"El total de Distancia es de:{totalDistacia}")
print(f"El promedio total de Tiempo es de:{promedioTiempo}")
print(f"El promedio total de Distancia es de:{promedioDistancia}")