'''
Registro de productos con validaciones
Escribí una función que permita registrar un nuevo producto en el inventario, pero con una
condición: la cantidad de productos debe ser mayor que 0 y el precio también debe ser un
valor positivo.
Al ingresar una cantidad o precio no válido, debe mostrar un mensaje de error y pedir los
datos nuevamente hasta que sean correctos.
'''

def validarCantidad():
    cantidad = int(input("Ingrese la cantidad de productos: "))
    while(not cantidad > 0):
        cantidad = int(input("La cantidad debe ser mayor a 0. Ingrese la cantidad de productos: "))
    return cantidad

def validarPrecio():
    precio = float(input("Ingrese el precio del producto: "))
    while(not precio > 0):
        precio = float(input("El precio debe ser mayor a 0. Ingrese el precio del producto: "))
    return precio

def registrar_producto():
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del producto: ")
    producto["cantidad"] = validarCantidad()
    producto["precio"] = validarPrecio()
    return producto

producto = registrar_producto()
print(producto)