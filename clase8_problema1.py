#Registro de ventas por día
'''
Desarrollá un programa que permita registrar las ventas diarias de un comercio durante 5 días. Al finalizar, el
sistema debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.

Tips:

Usá un bucle while que permita al usuario ingresar el monto de las ventas diarias.

Asegurate de validar que el monto ingresado sea un valor positivo.

Usá un acumulador para la suma de las ventas.
'''
##################################################
# inicializar
DIAS = 5
dia = 0
ventas = []

##################################################
# 
while(dia < DIAS):
    monto = float(input("ingresar el monto diario"))
    while(monto < 0):
        print("monto invalido")
        monto = float(input("ingresar el monto diario"))
    ventas.append(monto)
    dia+=1

##################################################
suma = 0
for monto in ventas:
    suma+=monto
promedio = suma / DIAS
    
