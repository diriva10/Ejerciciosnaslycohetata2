nombre=input("Digite tu Nombre:")
edad=int(input("Digite tu Edad:"))
sexo=input("Digite tu Sexo (femenino o masculino):")
estadoCivil=input("Estado Civil (solter@, casad@, separado o otro):")


if edad<18:
    print("Eres menor de edad no puedes votar")
elif edad>18 and sexo=="femenino" and estadoCivil=="casada":
    print("Puedes votar en la Mesa 1")
elif edad>18 and sexo=="femenino" and estadoCivil=="soltera":
    print("Puedes votar en la Mesa 2")
elif edad>18 and sexo=="femenino" and estadoCivil=="separada":
    print("Puedes votar en la Mesa 3")
elif edad>18 and sexo=="femenino" and estadoCivil=="otro":
    print("Puedes votar en la Mesa 4")
elif edad>18 and sexo=="masculino" and estadoCivil=="casado":
    print("Puedes votar en la Mesa 5")
elif edad>18 and sexo=="masculino" and estadoCivil=="soltero":
    print("Puedes votar en la Mesa 6")
elif edad>18 and sexo=="masculino" and estadoCivil=="separado":
    print("Puedes votar en la Mesa 7")
elif edad>18 and sexo=="masculino" and estadoCivil=="otro":
    print("Puedes votar en la Mesa 8")






