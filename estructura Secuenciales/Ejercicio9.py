#El propietario de una vivienda necesita renovar parte de esta, para lo cual tiene planeado
#enchapar los muros de los baños. La persona responsable de hacer este trabajo mide el
#alto y ancho de los muros. Se pide realizar un algoritmo para calcular el área del baño y el
#numero de baldosas necesarios para cubrir el baño. Sabiendo que la caja trae 3.5 metros
#cuadrados.
areaAltura=float(input("Ingrese el Area del baño altura:"))
areaBase=float(input("Ingrese la base del baño:"))

areaBano=areaAltura*areaBase/2

caja=3.5

cantidadBaldosas=areaBano/caja

print(f"Area del baño es:{areaBano}")

print(f"Las baldosas necesarias son:{cantidadBaldosas}")