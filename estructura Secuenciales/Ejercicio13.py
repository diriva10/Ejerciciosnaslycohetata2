#El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,
#25% Para construir vivienda, 15% para zonas verdes. Leer el área total del terreno en
#metros cuadrados e imprimir el área para cada destino, y el área que queda disponible
#para otros proyectos.

terreno=float(input("Digite el Area total del terreno:"))

cultivo=0.4
construVivienda=0.25
zonaVerde=0.15

areaClutivo=terreno*cultivo
areaConstruVivienda=terreno*construVivienda
areaZonaVerde=terreno*zonaVerde

print(f"El Area del Cultivo es:{areaClutivo}")
print(f"El Area de la Construcción de la vivienda es:{areaConstruVivienda}")
print(f"El Area de la Zona Verde es:{areaZonaVerde}")