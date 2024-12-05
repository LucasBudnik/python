#Gestión de inventario con diccionarios
'''
En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa
que permita:
1. Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un
diccionario donde la clave es el nombre del producto y el valor es su precio.
2. Una vez ingresados, mostrará todos los productos y sus precios en pantalla.
'''
products={}
product = input("Ingrese nombre de un nuevo producto(FIN='ZZZ'): ")
while product != "ZZZ":
    price = float(input("Ingrese precio del producto: "))
    products[product] = price
    product = input("Ingrese nombre de un nuevo producto(FIN='ZZZ'): ")

for product, price in products.items():
    print("Producto: ",product,", Price:",price)