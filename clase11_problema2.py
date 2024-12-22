#Cálculo de promedio de ventas
'''
Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:
1. Creá una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas
ventas.
2. Solicitá a la persona que ingrese las ventas de cada día durante una semana (7 días). Usá la función
para calcular y mostrar el promedio de ventas al finalizar.
'''
def promediar(ventas):
    return sum(ventas) / len(ventas)
DIAS = 7
ventas = []
for i in range(DIAS):
    ventas.append(float(input(f"Ingrese las ventas del día {i+1}: ")))

print("El promedio de ventas es:", promediar(ventas))
