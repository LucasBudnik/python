'''
1. Crear un menú interactivo

Crear un menú interactivo utilizando bucles while y condicionales if-elif-else:

El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la 
gestión de productos.
Entre las opciones, deben incluirse: 
- agregar productos al inventario y 
- mostrar los productos registrados.

2. Agregar productos al inventario
Implementar la funcionalidad para agregar productos a una lista:
Cada producto debe ser almacenado en una lista, y debe tener al menos 
- un nombre y una 
- cantidad asociada.

3. Mostrar el inventario

Mostrar los productos ingresados:

Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta
el momento.
'''
inventario = []
 #Menú
print("\t\tMenú de Opciones:\n\n")  
print("1. Agregar producto.") # OBLIGATORIA
print("2. Mostrar Productos.") # OBLIGATORIA
print("3. Buscar Producto por nombre.")
print("4. Eliminar Producto.")
print("5. Modificar Producto.")
print("6. Salir.")
print()
opcion = int(input("Ingrese opcion: "))
if(opcion == 6): 
    print("ha seleccionado la opción salir")
while(opcion != 6):
    #Selección de Opciones
    #----------------------------------------------------------
    if(opcion == 1): # AGREGAR UN PRODUCTO AL INVENTARIO
        volverAAgregar = "S" 
        while(volverAAgregar == "S")or(volverAAgregar == "s"):
            nombre = (input("Ingrese el nombre del producto: "))
            stock = int(input("Ingrese stock del producto (solo valores numericos): "))
            inventario.append([nombre, stock])
            volverAAgregar= input("¿Desea agregar otro producto? (S/N): ")
        '''INICIALIZAMOS LA OPCION DE VOLVER A AGREGAR EN S, 
        SI EL USUARIO QUIERE AGREGAR OTRO PRODUCTO VUELVE A SELECCIONAR LA OPCION S
        ACEPTAMOS TANTO S MAYUSCULA COMO s MINUSCULA'''


    #----------------------------------------------------------
    elif(opcion == 2): # MOSTRAR LOS PRODUCTOS EN EL INVENTARIO
        if (len(inventario) == 0):
            print("inventario vacio")
        else:
            indice = 0
            print("Inventario:")
            while(indice < len(inventario)):
                producto = inventario[indice]
                print(f"Nombre: {producto[0]}, Stock: {producto[1]}")
                indice+=1c 
    #----------------------------------------------------------
    elif(opcion == 3): # BUSCAR EL NOMBRE INGRESADO 
        nombre = input("Ingrese nombre a buscar: ")
        existe = False
        for producto in inventario:
            if producto[0] == nombre:  
                print("El producto está en la lista")
                existe = True
                break
        if not existe: 
            print(f"El producto {nombre} no está en el inventario")



    #----------------------------------------------------------
    elif(opcion == 4):# ELIMINAR EL NOMBRE INGRESADO
        nombre = input("Ingrese nombre a Eliminar: ")
        existe = False
        prod = ['zzz', 123]
        for producto in inventario:
            if producto[0] == nombre:  
                print("El producto esta en la lista")
                existe = True
                prod = producto
                break
        if existe: 
            inventario.remove(prod)
            print(f"El producto {nombre} ha sido eliminado")
        else: 
            print(f"El producto {nombre} no está en el inventario")



    #----------------------------------------------------------
    elif(opcion == 5): #MODIFICAR EL PRODUCTO
        nombre = input("Ingrese nombre a Modificar: ")
        existe = False
        indice = 0
        for producto in inventario:
            if producto[0] == nombre:  
                print("El producto esta en la lista")
                existe = True
                break
            indice+=1
        if existe:
            nombre = input("Ingrese Nuevo nombre: ")
            stock = int(input("Ingrese nuevo stock: "))
            inventario[indice] = [nombre,stock]
        else: 
            print(f"El producto {nombre} no está en el inventario")
    


    #----------------------------------------------------------
    elif(opcion == 6):
        print("ha seleccionado la opción de salir")
    


    #----------------------------------------------------------
    else:
        print("Opción seleccionada invalida")



    #----------------------------------------------------------
    if(opcion != 6):
         #Menú
        print("\t\tMenú de Opciones:\n\n")  
        print("1. Agregar producto.") # OBLIGATORIA
        print("2. Mostrar Productos.") # OBLIGATORIA
        print("3. Buscar Producto por nombre.")
        print("4. Eliminar Producto.")
        print("5. Modificar Producto.")
        print("6. Salir.")
        print()
        opcion = int(input("Ingrese opcion: "))
        if(opcion == 6): 
            print("ha seleccionado la opción salir")
