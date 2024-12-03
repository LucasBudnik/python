
#Mostrar los códigos de productos ingresados
'''
En un sistema de inventario, cada producto tiene un código que lo identifica. Escribí un
programa que permita ingresar los códigos de 4 productos y luego mostrálos uno por uno,
junto con su posición en la lista.
Ejemplo: si los códigos ingresados son
"P001", "P002", "P003", "P004", el programa
debe mostrar:
Producto 1: P001
Producto 2: P002
Producto 3: P003
Producto 4: P004

Tips:
● Utilizá un bucle for y range() para recorrer los códigos e imprimirlos.
'''


productos = int(input("Ingrese cuantos productos desea agregar: "))
codigo = []
for i in range(productos):
    codigo.append(input("Ingrese el código del producto: "))
for i in range(len(codigo)):
    print(f"Producto {i+1}: {codigo[i]}")