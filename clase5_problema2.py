#Compra con descuentos

#Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de
#artículos que está comprando. El programa debe determinar el descuento aplicable según las siguientes
#reglas:
monto=float(input("Ingrese monto total de compra $"))
cantidad=int(input("Ingrese cantidad de articulos "))


#Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000,
#aplica un descuento del 15%.
#Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento
#del 10%.
#Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.


descuento = 0
if(cantidad >= 5)and(monto > 10000):
    descuento = (15*monto)/100
elif (cantidad >= 3)and(cantidad < 5):
    descuento = (10*monto)/100
monto_total = monto - descuento
print("El monto total a pagar es: ", monto_total,"$")

#Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier
#descuento o simplemente el monto original si no hay descuento.
