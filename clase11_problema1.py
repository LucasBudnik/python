# Gestión de Descuentos

'''
Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. Vas a desarrollar un
programa que permita calcular el precio final de un producto después de aplicar un descuento. Para hacerlo:

1. Crea una función que reciba como parámetros 

recibe
el precio original del producto y 
el porcentaje de descuento, 

y que retorne 
el precio final con el descuento aplicado.

2. Luego, pedí que se ingrese el precio y el porcentaje de descuento. 
Mostrá el precio final después de aplicar el descuento.
'''

# El descuento realizado es el precio original menos el precio original por el porcentaje de descuento dividido 100
def descontar(precio, descuento):
    return precio - (precio * descuento / 100)

precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

print("El precio final con el descuento aplicado es:", descontar(precio, descuento))
