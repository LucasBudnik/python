#Usando la instrucción print() y lo visto en la clase,
#escribir un programa que muestre en la terminal la
#lista de productos que necesitamos comprar en el
#supermercado.

#Escribir un programa que guarde en variables el
#monto del ingreso de cada uno de los primeros 6
#meses del año.

#Luego, calcular y guardar en otra variable el
#promedio de esos valores.

#Por último, mostrar una leyenda que diga “El
#ingreso promedio en el semestre es de xxxxx”
#donde “xxxxx” es el valor calculado.

enero = float(input("ingrese monto de enero "))
febrero = float(input("Ingrese el monto de febrero "))
marzo = float(input("ingrese monto de marzo "))
abril = float(input("Ingrese el monto de abril "))
mayo = float(input("ingrese monto de mayo "))
junio = float(input("Ingrese el monto de junio "))
print("enero: ",enero)
print("febrero: ", febrero)
print("marzo: ", marzo)
print("abril: ", abril)
print("mayo: ", mayo)
print("junio: ", junio)
suma = enero + febrero + marzo + abril + mayo + junio
promedio = suma / 6
#print(f"El ingreso en los primeros 6 meses del año es de {suma} \n por lo tanto en promedio tenemos: {promedio}")
print(" El ingreso promedio en el semestre es de", promedio)
print(f"El ingreso promedio en el semestre es de {promedio}")
# Como vemos de ambas formas se puede imprimir el mensaje