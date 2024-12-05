# Consultar stock en inventario
'''
El inventario de una tienda está almacenado en un diccionario, donde las claves son los
nombres de los productos y los valores son las cantidades disponibles en stock. Creá un
programa que:
    
    1.Te permita ingresar el nombre de un producto.

    2.Utilice el método .get() para buscar el stock disponible. Si el producto no existe, deberá
    mostrar un mensaje diciendo "Producto no encontrado".

    3.Si el producto está disponible, mostrará cuántas unidades quedan en stock.

'''

products = {}
product = input("Ingrese nombre de un nuevo producto(FIN='ZZZ'): ")

while product != "ZZZ":
    stock = int(input("Ingrese stock del producto: "))
    products[product] = stock
    product = input("Ingrese nombre de un nuevo producto(FIN='ZZZ'): ")

for product, stock in products.items():
    print("Producto: ",product,", Stock:",stock)

Indice = input("Ingrese nombre de producto para verificar stock disponible(FIN='ZZZ'):")
while (Indice != 'ZZZ'):
    result = products.get(Indice, 0)
    
    if result == 0:
        print("El producto no está disponible")
    else: 
        print("El producto está disponible, quedan",result,"unidades en stock")

    Indice = input("Ingrese nombre de producto para verificar stock disponible(FIN='ZZZ'):")