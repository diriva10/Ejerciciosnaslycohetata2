'''En clase de programación, se sacan 4 notas del 15%,30%,30%,25% respectivamente. Se
pide diseñar un algoritmo que permita mostrar la nota definitiva de un estudiante.
Teniendo en cuenta que la primera nota consta del promedio de dos talleres, la segunda
de tres evaluaciones, la tercera nota de un trabajo final y la última es el promedio de 4
quizzes.'''

notaTaller1=float(input("Ingrese la calificación del 1 taller:"))
notaTaller2=float(input("Ingrese la calificación del 2 taller:"))

evaluacion1=float(input("Ingrese la calificación de la 1 Evaluación:"))
evaluacion2=float(input("Ingrese la calificación de la 2 Evaluación:"))
evaluacion3=float(input("Ingrese la calificación del 3 Evaluación:"))

notaTrabajoFinal=float(input("Ingresa la nota del trabajo Final:"))

notaQuizz1=float(input("Ingrese la nota del primer quizz:"))
notaQuizz2=float(input("Ingrese la nota del segundo quizz:"))
notaQuizz3=float(input("Ingrese la nota del tercer quizz:"))
notaQuizz4=float(input("Ingrese la nota del cuarto quizz:"))

nota1=notaTaller1+notaTaller2/2
nota2=evaluacion1+evaluacion2+evaluacion3/3
nota3=notaTrabajoFinal
nota4=notaQuizz1+notaQuizz2+notaQuizz3+notaQuizz4/4

notaDefinitiva=(nota1*0.15)+(nota2*0.30)+(nota3*0.30)+(nota4*0.25)

print(f"La nota final es de:{notaDefinitiva}")