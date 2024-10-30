#Control de Stock de productos

#Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock
#que hay de cada uno. El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida
#salir, ingresando "salir" como nombre de producto. Después de que el bucle termine, el programa debe mostrar
#la cantidad total de productos ingresados.
cant_total = 0
nom = input("Ingrese nombre del producto ")
while(nom != "salir"):
    cant = int(input("Ingrese cantidad de productos "))
    cant_total += cant
    nom = input("Ingrese nombre del producto ")
print("La cantidad total de productos ingresados es de ", cant_total)







#Tips:

#Vas a necesitar un contador.

#Tené presente las estructuras condicionales.