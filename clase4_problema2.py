#Consumo de Combustible

#Realizar una aplicación en Python que;

#A partir de la cantidad de litros de combustible que
#consume un coche por cada 100 km de recorrido,
#el costo de cada litro de combustible y la longitud
#del viaje realizado (en kilómetros), muestra un
#detalle de los litros consumidos y el dinero
#gastado.

litrosConsumidos = float(input("Cantidad de litros consumidos por cada 100km (l/100km) "))
costoLitro = float(input("Valor del costo por litro ($/l) "))
longitudViaje = float(input("longitud del viaje (km) "))


# suponiendo que tengo la cantidad de litros consumidos por cada 100km
# calculo la cantidad de litros consumidos por cada 1 km dividiendo por 100
consumoPorKilometro = litrosConsumidos / 100
print (" La cantidad consumida en promedio por kilometro es de ", consumoPorKilometro,"l/km")
# obtengo la cantidad de litros consumidos promedio por kilometro, eso lo multiplico
# por la longitud del viaje en kilometros
consumoTotal = consumoPorKilometro * longitudViaje
print (" Por lo tanto la cantidad de litros consumidas en todo el viaje seria de ", consumoTotal,"l")
# al tener la cantidad de litros consumidos en todo el viaje lo multiplico por el 
# costo por litro y obtengo el costo de la longitud del viaje 
costoFinal = costoLitro * consumoTotal
print (" El costo total del viaje seria de ", "{:.2f}".format(costoFinal),"$")