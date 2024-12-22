import sqlite3

def inicializar_bd():
    connect = sqlite3.connect("productos.db")
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products  ''')