#Una madre y sus 4 hijos se acercan a recibir información por parte de un abogado
#referente al dinero que les corresponde en una herencia dejada por su esposo y padre
#respectivamente.

nombreMadre=input("Ingrese el Nombre de la Madre:")
nombreHijo1=input("Ingrese el Nombre del Primer Hijo:")
nombreHijo2=input("Ingrese el Nombre del Segundo Hijo:")
nombreHijo3=input("Ingrese el Nombre del Tercer Hijo:")
nombreHijo4=input("Ingrese el Nombre del Cuarto Hijo:")

monto=float(input("Ingrese el Monto de la Herencia"))

porcientoMadre=0.5
porcientoHijos=0.5

totalMadre=monto*porcientoMadre
totalHijos=monto*porcientoHijos/4

print(f"A la Madre:{nombreMadre},Le pertenece:{totalMadre} ")
print(f"Y a sus hijos:{nombreHijo1,nombreHijo2,nombreHijo3,nombreHijo4,},le pertenece:{totalHijos}.")
