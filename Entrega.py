# Entrega de Proyecto Final
'''
1. Registro de productos: Ingresar nuevos productos al
inventario, solicitando nombre, descripción, cantidad
disponible, precio y categoría.

2. Consulta de productos: Consultar el inventario y
ver la información detallada de cada producto, como
stock disponible y precio.

3. Actualización de productos: Modificar la
cantidad disponible de un producto específico.

4. Eliminación de productos: Permitir eliminar
productos del inventario.

5. Listado Completo: Generar un listado completo
del inventario.

6. Reporte de Bajo Stock: Mostrar un reporte de
productos con bajo stock.

'''

import sqlite3
from colorama import init,Fore,Back,Style
init(autoreset=True)
#----------------------------------------------------------------
#FUNCIONES
#----------------------------------------------------------------
#FUNCION MENU: MUESTRA EL MENU DE OPCIONES CON LA MEJOR INTERFAZ Y DEVUELVE LA OPCION SELECCIONADA
def Menu():
    print(Fore.YELLOW + "\t\tMenú de Opciones:\n\n")  
    print(Fore.YELLOW + "1. Agregar producto.") # OBLIGATORIA
    print(Fore.YELLOW + "2. Mostrar Productos.") # OBLIGATORIA
    print(Fore.YELLOW + "3. Buscar Actualizar Producto.")
    print(Fore.YELLOW + "4. Eliminar Producto.")
    print(Fore.YELLOW + "5. Listado Completo.")
    print(Fore.YELLOW + "6. Reporte de Bajo Stock.")
    print(Fore.YELLOW + "7. Salir.")
    print()
    opcion = int(input("Ingrese opcion: "))
    return opcion
#----------------------------------------------------------------
#REGISTRO DE PRODUCTOS 1
def RegistroProductos():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    stock = int(input("Ingrese el stock del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoria del producto: ")
    return nombre, descripcion, stock, precio, categoria

#----------------------------------------------------------------
#CONSULTA DE PRODUCTOS 2
def ConsultaProductos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return productos

#----------------------------------------------------------------
#ACTUALIZACION DE PRODUCTOS 3
def ActualizacionProductos():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    stock = int(input("Ingrese el nuevo stock del producto: "))
    cursor.execute("UPDATE productos SET stock = ? WHERE nombre = ?", (stock, nombre))
    conn.commit()
    print("Producto actualizado correctamente")

#----------------------------------------------------------------
#ELIMINACION DE PRODUCTOS 4
def EliminacionProductos():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
    conn.commit()
    print("Producto eliminado correctamente")

#----------------------------------------------------------------
#LISTADO COMPLETO DE PRODUCTOS 5
def ListadoCompletoProductos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return productos

#----------------------------------------------------------------
#REPORTES DE BAJO STOCK 6
def ReporteBajoStock():
    cursor.execute("SELECT * FROM productos WHERE stock < 10")
    productos = cursor.fetchall()
    return productos


#----------------------------------------------------------------
#SELECCION DE OPCIONES 
def selector(opcion, cursor, conn):
    while opcion != 7:
        if opcion == 1:
            producto = RegistroProductos()
            cursor.execute("INSERT INTO productos
            (producto) VALUES (?, ?, ?)",
            (nombre, descripcion, stock, precio, categoria)
            )
            conn.commit()
        elif opcion == 2:
            ConsultaProductos()
        elif opcion == 3:
            ActualizacionProductos()
        elif opcion == 4:
            EliminacionProductos()
        elif opcion == 5:
            ListadoCompletoProductos()
        elif opcion == 6:
            ReporteBajoStock()
        elif opcion == 7:
            print("Gracias por usar el sistema")
        else:
            print("Opcion no valida")

#--------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------PROGRAMA PRINCIPAL----------------------------------------------------------------
#CONEXION A LA BASE DE DATOS
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

#----------------------------------------------------------------
#MENU DE OPCIONES
opcion = Menu()
selector(opcion)
conn.close()