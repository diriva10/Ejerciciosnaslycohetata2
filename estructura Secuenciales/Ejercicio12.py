#El testamento tiene las siguientes condiciones: A la esposa le corresponde el 40% mientras
#que a los hijos les corresponde: 30% 20% 40% 10% respectivamente. Se pide un algoritmo
#que lea los datos necesarios, y muestre lo que le corresponde a la esposa y a los hijos.

nombreMadre=input("Ingrese el Nombre de la Madre:")
nombreHijo1=input("Ingrese el Nombre del Primer Hijo:")
nombreHijo2=input("Ingrese el Nombre del Segundo Hijo:")
nombreHijo3=input("Ingrese el Nombre del Tercer Hijo:")
nombreHijo4=input("Ingrese el Nombre del Cuarto Hijo:")

monto=float(input("Ingrese el Monto de la Herencia:"))

porcentajeMadre=0.4
porcentajeHijo1=0.3
porcentajeHijo2=0.2
porcentajeHijo3=0.4
porcentajeHijo4=0.1

exEsposa=monto*porcentajeMadre
hijo1=monto*porcentajeHijo1/100
hijo2=monto*porcentajeHijo2/100
hijo3=monto*porcentajeHijo3/100
hijo4=monto*porcentajeHijo4/100

print(f"La herencia de la Madre es:{exEsposa}")
print(f"La herencia del Hijo es:{nombreHijo1} con un {hijo1}")
print(f"La herencia del Hijo es:{nombreHijo2} con un {hijo2}")
print(f"La herencia del Hijo es:{nombreHijo3} con un {hijo3}")
print(f"La herencia del Hijo es:{nombreHijo4} con un {hijo4}")