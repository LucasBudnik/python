'''
    Crea un programa que cree varios registros en la tabla Personas
    usando una lista de tuplas predefinidas
    con los campos; 
    nombre,
    edad,
    ciudad.
    usa un bucle para recorrer la lista e insertar cada persona en la base de datos
    La lista debe tener almenos 5 personas nuevas y al finalizar se deben mostrar
    todas las personas en la base de datos.
'''
import sqlite3 # Importar el módulo
conexion = sqlite3.connect("Personas.db") # Conectar a la base de datos (o crearla)
cursor = conexion.cursor()


 # Crear un cursor para interactuar con la base de datos
cursor.execute('''CREATE TABLE IF NOT EXISTS personas 
               (nombre TEXT NOT NULL, 
               edad INTEGER NOT NULL, 
               ciudad TEXT NOT NULL)
               ''')
conexion.commit()

# Crear una lista de tuplas con los datos de las personas
nuevas_personas = [
    ("Esteban", 32, "Mar del Plata"),
    ("Valeria", 27, "Bahía Blanca"),
    ("Fernando", 41, "Rosario"),
    ("Carolina", 29, "La Plata"),
    ("Juan", 35, "Córdoba")
 ]

# recorremos la lista de tuplas e insertamos de a una tupla
for persona in nuevas_personas:
    cursor.execute("INSERT INTO Personas (?,?,?) VALUES", persona)
    conexion.commit()

# Mostrar todas las personas en la base de datos
cursor.execute("SELECT * FROM personas")
persona = cursor.fetchall()
print(persona)

conexion.close()
