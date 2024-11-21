lado1=float(input("Digite el numero del primer lado de su tringulo:"))
lado2=float(input("Digite el numero del segundo lado de su tringulo:"))
lado3=float(input("Digite el numero del tercer lado de su tringulo:"))


if (lado1<lado2+lado3) and (lado2<lado1+lado3) and (lado3<lado1+lado2):
    print("Es un triangulo:")

elif lado1!=lado2 and lado2!=lado3:
    print("Es un triangulo escaleno")
    
    
    
