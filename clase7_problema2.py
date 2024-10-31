# Consultar el stock de productos
'''
Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en
stock. Si el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando
que no está disponible.

Tips:

Usá una lista para almacenar los productos en stock.

Permití que el usuario ingrese el nombre de un producto a consultar.

Recorré la lista con un bucle while para verificar si el producto está en stock.
'''

# producto: el nombre de los productos con stock
# productos: la lista de productos con stock
# opcion: habilitador para buscar producto
# puntero: variable indice para recorrer la lista e ir comparando


######################################################################################
# INICIALIZAMOS
productos = []
producto = input("Ingrese nombre de producto en stock (FIN='ZZZ'): ")

######################################################################################
# EL USUARIO INGRESA EL NOMBRE DEL PRODUCTO HASTA QUE INGRESE EL NOMBRE DEL PRODUCTO 'ZZZ'
while(producto != "ZZZ"):
    productos.append(producto)
    producto = input("Ingrese nombre de producto en stock(FIN='ZZZ'): ")



######################################################################################
# OPCION PARA BUSCAR PRODUCTO POR PRIMERA VEZ
opcion = input("Ingrese si desea buscar un producto (S/N): ")
while(opcion == "S")or(opcion == "s"):


    ###########################################
    #BUSQUEDA DEL PRODUCTO
    producto = input("Ingrese nombre del producto a buscar: ")
    puntero = "ZZZ" # INICIALIZAMOS X EN UN PRODUCTO QUE NO ESTA EN LA LISTA
    indice = 0
    while(puntero != producto)and(indice < len(productos)):
        puntero = productos[indice]
        if puntero == producto:
            print("El producto está en stock")
        indice+=1
    # EN CASO DE QUE RECORRAMOS TODA LA LISTA Y NO ENCONTREMOS EL PRODUCTO:
    if puntero != producto: print ("El producto no está en stock")

    ###########################################
    
    
    
    # OPRCION PARA BUSCAR OTRO PRODUCTO
    opcion = input("Ingrese si desea buscar otro producto (S/N): ")
######################################################################################