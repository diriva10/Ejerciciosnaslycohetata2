puntajeMate=float(input("Ingrese el puntaje de Matemáticas:"))
puntajeLengua=float(input("Ingrese el puntaje de Lenguaje:"))

if puntajeMate>puntajeLengua:
    print(f"El puntaje más alto es:{puntajeLengua}")
elif puntajeLengua>puntajeMate:
    print(f"El puntaje más alto es:{puntajeMate}")
elif puntajeLengua==puntajeMate:
    print("El resultado de ambas son iguales")
