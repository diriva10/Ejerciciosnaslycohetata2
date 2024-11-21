#Una cancha de futbol fue ampliada en un 20%. Determinar el área total en metros de lacancha.

LargoOriginal=float(input("Digite el largo de la cancha:"))
AnchoOriginal=float(input("Digite el ancho de la cancha:"))

AreaOriginal=LargoOriginal*AnchoOriginal

print(f"Area Original:{AreaOriginal}metros cuadrados")

aumento=0.20

operacion=AreaOriginal*(1+aumento)

areanueva=AreaOriginal+operacion
print(f"Area nueva:{areanueva}metros cuadrados")
