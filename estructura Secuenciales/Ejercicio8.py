#Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al
#segundo operador. El cliente desea conocer el costo de cada llamada, El costo total de las
#llamadas a cada operador, y el total de las cuatro llamadas.

CostoOperador1=float(input("Ingrese el costo de Minutos que obtuvo de su primer operador:"))
CostoOperador2=float(input("Ingrese el costo de Minutos que obtuvo de su segundo operador:"))

Duracion1=float(input("Ingrese la duración de la primera llamada del Operador 1:"))
Duracion2=float(input("Ingrese la duración de la segunda llamada del Operador 1:"))
Duracion3=float(input("Ingrese la duración de la tercera llamada del Operdor 2 :"))
Duracion4=float(input("Ingrese la duración de la cuarta llamada del Operador 2 :"))

CostoCadaLlamada1=Duracion1*CostoOperador1
CostoCadaLlamada2=Duracion2*CostoOperador1
CostoCadaLlamada3=Duracion3*CostoOperador2
CostoCadaLlamada4=Duracion4*CostoOperador2

CostoTotalOpera1=CostoCadaLlamada1+CostoCadaLlamada2
CostoTotalOpera2=CostoCadaLlamada3+CostoCadaLlamada4

CostoTotal=CostoTotalOpera1+CostoTotalOpera2

print(f"Costo llamada 1 al Operador 1:{CostoCadaLlamada1}")
print(f"Costo llamada 2 al operador 1:{CostoCadaLlamada2}")
print(f"Costo llamada 3 al Operador 2:{CostoCadaLlamada3}")
print(f"Costo llamada 4 al operador 2:{CostoCadaLlamada4}")
print(f"Costo total operador 1:{CostoTotalOpera1}")
print(f"Costo total operador 2:{CostoTotalOpera2}")
print(f"Costo Total de las dos Operadoras son de:{CostoTotal}")








