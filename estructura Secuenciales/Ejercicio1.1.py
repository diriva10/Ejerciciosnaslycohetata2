#A un empleado le aplican una retención del 18% sobre su salario básico, y le entregan una
#Bonificación de 1.3% sobre el salario. Desarrolle un algoritmo que permita calcular e
#imprimir el salario neto y los valores de sus respectivos porcentajes.

salario=int(input("Digite el salario:"))
retencion=salario* 0.18
#salarioRetencion=salario-retencion
bonificacion=salario* 0.013
#salarioBonificacion=salario+bonificacion
salarioNeto=(salario-retencion)+bonificacion
print("El salario Neto es:",salarioNeto)
print("El salario Retencion es:",retencion)
print("El salario bonificaciòn es: ",bonificacion)
