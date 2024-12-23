# Entrega de Proyecto Final
import sqlite3
from colorama import init,Fore,Back,Style
import random
init(autoreset=True)

#Aclaraciones, 
#se usaron try-excepts
#La introduccion de datos se dejo automatica para poder probarlo sin necesidad de ir dato por dato
#aplicando los conocimientos adquiridos del uso de la libreria random

#----------------------------------------------------------------
# Definición de estilos globales
HEADER = Fore.YELLOW + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
INFO = Fore.CYAN + Style.NORMAL
RESET = Style.RESET_ALL
# Al ser un agregado podemos generarlo como global, (igual no lo considero una buena práctica el uso de variables globales)
#----------------------------------------------------------------
#FUNCIONES
#----------------------------------------------------------------
#FUNCION MENU: MUESTRA EL MENU DE OPCIONES CON LA INTERFAZ SELECCIONADA
def Menu():
    print(HEADER + "#################################################")
    print(HEADER + "#\t\tMenú de Opciones:\t\t#")  
    print(HEADER +"#################################################")
    print(INFO + "\t1. Agregar producto.")
    print(INFO + "\t2. Consultar Productos.")
    print(INFO + "\t3. Actualización de Producto.")
    print(INFO + "\t4. Eliminación Producto.")
    print(INFO + "\t5. Listado Completo.")
    print(INFO + "\t6. Reporte de Bajo Stock.")
    print(ERROR+"\t7. Salir.\n")
    opcion = input(INFO + "Ingrese opción: ")
    return opcion
#----------------------------------------------------------------
#REGISTRO DE PRODUCTOS 1
def RegistroProductos():
    print(SUCCESS +"#----------------------------------------------------------------\n#REGISTRO DE PRODUCTOS")
    # se Enlaza el archivo de base de datos
    conexion = sqlite3.connect('inventario.db')
    # Creamos el cursor para interactuar con la base de datos    
    cursor = conexion.cursor()
    # Codigo sqlite: se crea la Tabla en base de datos   
    insert = '''
        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, 
        descripcion TEXT, 
        stock INTEGER NOT NULL, 
        precio FLOAT NOT NULL, 
        categoria TEXT
        )
    '''
    # se ejecuta el codigo sql
    cursor.execute(insert)
    # se generan productos aleatorios
    NOMBRES = [
    "Manzana",
    "Zanahoria",
    "Tomate",
    "Atún enlatado",
    "Gaseosa",
    "Snack de Maíz",
    "Barra de Granola",
    "Cereal Integral",
    "Aceite de Oliva",
    "Yogur Natural"
    ]   
    CATEGORIAS = ["FRUTAS", "VERDURAS", "PRODUCTOS ENLATADOS", "BEBIDAS", "SNACKS"]
    DESCRIPCIONES = [
    "Producto fresco y delicioso, ideal para cualquier ocasión.",
    "Sabor natural y auténtico, perfecto para disfrutar en cualquier momento.",
    "Rico en nutrientes, una excelente opción para complementar tu dieta.",
    "Práctico y fácil de usar, ideal para llevar contigo a donde vayas.",
    "Una opción sabrosa y saludable, perfecta para satisfacer tus antojos.",
    "Versátil y delicioso, se adapta a diversas recetas y preparaciones.",
    "Calidad garantizada, ideal para disfrutar solo o en compañía.",
    "Fresco y nutritivo, perfecto para un estilo de vida saludable."
    ]
    nombre = random.choice(NOMBRES)
    descripcion = random.choice(DESCRIPCIONES)
    stock = random.randint(0, 100)
    precio = random.uniform(10.5, 100.5)
    categoria = random.choice(CATEGORIAS)
    
    # se crea codigo sql para introducir los productos aleatorios
    insert = "INSERT INTO productos (nombre, descripcion, stock, precio, categoria) VALUES (?,?,?,?,?)"
    
    # se ejecuta el codigo sql con los parametros aleatorios
    conexion.execute(insert,(nombre, descripcion, stock, precio, categoria))
    # Se muestra lo que se cargo en la base de datos
    print(SUCCESS + f'''nombre:{nombre}\ndescripcion:{descripcion}\nstock:{stock}\nprecio:{precio}\ncategoria:{categoria}\n ''')
    # commit
    conexion.commit()
    # close
    conexion.close()
#----------------------------------------------------------------
# CONSULTAR PRODUCTOS
def ConsultaProductos():
    print(SUCCESS + "#----------------------------------------------------------------\n#CONSULTAR PRODUCTOS")
    # se conecta con la base de datos
    conexion = sqlite3.connect('inventario.db')
    # se crea el cursor
    cursor = conexion.cursor()
    # se ingresa el nombre del producto a conocer en detalle
    nombre = input(SUCCESS + "Ingrese el nombre del producto a consultar: ")
    # se crea el codigo sql para consultar los productos
    select = "SELECT * FROM productos WHERE nombre = ?"
    # se ejecuta el codigo sql  
    cursor.execute(select,(nombre,))
    # se obtiene el resultado de la consulta
    resultado = cursor.fetchone()
    # se muestra el resultado
    if resultado:
        print(INFO+f"nombre: {resultado[1]} stock: {resultado[3]} precio: {resultado[4]}$")
    else: print(ERROR+f"No se encuentran resultados con {nombre}")
#----------------------------------------------------------------
#ACTUALIZAR PRODUCTOS 3
def ActualizacionProductos():
    print(SUCCESS + "#----------------------------------------------------------------\n#ACTUALIZACION DE PRODUCTOS")
    # se crea la conexion con el archivo base de datos
    conexion = sqlite3.connect('inventario.db')
    # se crea el cursor para interactuar con la base de datos
    cursor = conexion.cursor()
    # se lee un nombre desde teclado para buscar en la base de datos
    nombre = input(INFO+"Nombre del producto: ")
    

    cursor.execute("SELECT nombre FROM productos WHERE nombre = ?",(nombre,))
    if (cursor.fetchone()):
        # se lee el stock que deseamos actualizar
        nuevo_stock = int(input(INFO+"Nuevo stock: "))
        # se ejecuta el codigo para actualizar la base de datos
        ACTUALIZAR = "UPDATE productos SET stock = ? WHERE nombre = ?"
        cursor.execute(ACTUALIZAR,(nuevo_stock, nombre))
    else:
        print(ERROR + "El nombre ingresado no tiene candidatos para modificar")
    # se efectua el commit correspondiente
    conexion.commit()
    # se cierra la conexion
    conexion.close()

#----------------------------------------------------------------
#ELIMINACION DE PRODUCTOS 4
def EliminacionProductos():
    print(SUCCESS + "#----------------------------------------------------------------\n#ELIMINACION DE PRODUCTOS")
    # Vincular con el archivo de base de datos
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    #----------------------------------------------------------------
    # Se Verifica si la tabla existe
    VERIF = "SELECT name FROM sqlite_master WHERE type='table' AND name ='productos';"
    cursor.execute(VERIF)
    if cursor.fetchone() is None:
        print(ERROR+"La tabla 'productos' no existe. Asegúrate de crearla primero.")
        conexion.close()
        return
    #----------------------------------------------------------------
    # Leer el nombre del producto que se desea eliminar
    nombre = input(INFO + "Ingrese el nombre del producto a eliminar: ")
    # Crear el código para eliminar producto por nombre
    ELIMINAR = "DELETE FROM productos WHERE nombre = ?"
    # validamos mediante try-except si el codigo elimina correctamente
    try:
        cursor.execute(ELIMINAR, (nombre,))
        print(SUCCESS + "eliminacion exitosa")
    except Exception as e:
        print("Error al eliminar el producto:", e)
    # Realizar el commit y cerrar la conexión
    conexion.commit()
    conexion.close()

#----------------------------------------------------------------
# LISTADO COMPLETO 5
def ListadoCompletoProductos():
    print(SUCCESS + "#----------------------------------------------------------------\n#LISTADO COMPLETO DE PRODUCTOS")
    # se conecta con el archivo de base de datos
    conexion = sqlite3.connect('inventario.db')
    # se activa el cursor para poder interactuar con la base de datos
    cursor = conexion.cursor()
    # se ejecuta la solicitud de todos los productos que hay en la base de datos
    cursor.execute("SELECT * FROM productos")
    # tomamos todos los productos solicitados
    productos = cursor.fetchall()
    # se recorre la lista de productos obtenida y los va mostrando
    for product in productos:
        # Acceder a los elementos de la tupla
        print(INFO + f"ID: {product[0]}, Nombre: {product[1]}, Descripción: {product[2]}, Stock: {product[3]}, Precio: {product[4]}, Categoría: {product[5]}")
    # último pero no menos importante, se cierra la conexión
    conexion.close()


#----------------------------------------------------------------
# REPORTE DE BAJO STOCK 6
def ReporteBajoStock():
   # se conecta con el archivo de base de datos
   conexion = sqlite3.connect('inventario.db')
   # se crea la variable para interactuar con la base de datos
   cursor = conexion.cursor()

   SOLICITUD_MENOR_STOCK ="SELECT nombre, stock FROM productos WHERE stock < ?"
   try:
        limite = int(input(INFO + "ingrese el valor a partir del cual se considera bajo stock "))
        cursor.execute(SOLICITUD_MENOR_STOCK, (limite,))
   except ValueError:
        print(ERROR+"Por favor, ingrese un número válido.")
   except Exception as e:
        print(ERROR+"Error al ejecutar la consulta:", e)
   # Se obtienen todos los datos que cumplen con las caracteristicas pedidas:
   productos = cursor.fetchall()
   # se recorre la lista de productos obtenida y los va mostrando
   if productos:  # Verifica si hay productos en la lista
        for product in productos:
            # Formatear la salida para mostrar el nombre y el stock
            print(ERROR + f"Producto: {product[0]}, Stock: {product[1]}")
   else:
        print(INFO + "No hay productos con bajo stock.")
   conexion.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------PROGRAMA PRINCIPAL----------------------------------------------------------------
#----------------------------------------------------------------
#MENU DE OPCIONES
opcion = Menu()
while opcion != 7:
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            RegistroProductos()
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
            print(SUCCESS+"Gracias por usar el sistema")
            break
        else:
            print(ERROR + "Opción no válida")
    else:
        print(ERROR + "Opción no válida. Por favor, ingrese un número del 1 al 7.")
    opcion = Menu()