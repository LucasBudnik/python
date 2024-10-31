'''
Ahora, vamos a analizar un ejemplo que nos será útil para el TFI: usaremos un bucle while y una lista de listas
para ingresar datos de varios productos al inventario.

El script comienza creando una lista vacía llamada productos, que va a almacenar los datos de los productos
ingresados. Luego, pide al usuario que ingrese el código del producto, que es un número entero. El bucle while
se utiliza para controlar la repetición del proceso de entrada de datos: mientras el usuario no ingrese un código
igual a 0, el ciclo sigue ejecutándose.

Cada vez que el usuario ingresa un código válido, el script pide: 
- descripción del producto.
- precio.
- cantidad que está siendo ingresada. 
Estos cuatro datos se almacenan como una lista dentro de la lista productos,
lo que permite agrupar todos los datos de un mismo producto.
'''

productos = []
codigo = int(input("Ingrese Código(FIN='0'): "))
producto = []
while (codigo != 0):
    descripcion = input("Ingrese descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = [codigo, descripcion, precio, cantidad]
    productos.append(producto)
    codigo = int(input("Ingrese Código(FIN='0'): "))

for x in productos:
    print(x)
    
