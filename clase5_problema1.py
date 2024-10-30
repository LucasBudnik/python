#Control de inventario de una tienda de videojuego

#Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario.dueño te pide que escribas
#un programa que verifique si hay stock suficiente de un videojuego y, si no hay, que avise que hay que
#reponerlo.

#El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad,
#mostrar si se necesita hacer un nuevo pedido o no.

stock=int(input("Ingrese la cantidad de stock actual "))
cantidadDeStockNecesaria=5
if(stock < cantidadDeStockNecesaria):
    print("Se necesita hacer un nuevo pedido")
else:
    print("La cantidad de stock es suficiente")