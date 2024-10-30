#Ticket de la compra

#Escribir un programa que solicite el nombre, la
#cantidad y el valor unitario de tres productos.
nombre1=input(("Ingrese nombre del producto uno: "))
cantidad1=int(input("Ingrese cantidad del producto uno: "))
valor1=float(input("Ingrese valor unitario del producto uno: "))

nombre2=input(("Ingrese nombre del producto dos: "))
cantidad2=int(input("Ingrese cantidad del producto dos: "))
valor2=float(input("Ingrese valor unitario del producto dos: "))

nombre3=input(("Ingrese nombre del producto tres: "))
cantidad3=int(input("Ingrese cantidad del producto tres: "))
valor3=float(input("Ingrese valor unitario del producto tres: "))
#Luego, debe calcular el importe de IVA (21%)
#de cada producto.
precio1 = cantidad1*valor1
precio2 = cantidad2*valor2
precio3 = cantidad3*valor3

iva1=(precio1*21)/100
iva2=(precio2*21)/100
iva3=(precio3*21)/100

tot1 = precio1 + iva1
tot2 = precio2 + iva2
tot3 = precio3 + iva3

tot = tot1 + tot2 + tot3
#Por último, debe mostrar en la terminal el
#ticket de la operación con todos los datos de la
#compra.

print("Ticket de la compra:\n")
print("-----------------------------------------")
print("Name\t val\t cant\t Precio\t iva(21%)\t Subtotal")
print(nombre1, "\t", valor1, "\t", cantidad1, "\t", precio1, "\t", iva1, "\t\t", tot1)
print(nombre2, "\t", valor2, "\t", cantidad2, "\t", precio2, "\t", iva2, "\t\t", tot2)
print(nombre3, "\t", valor3, "\t", cantidad3, "\t", precio3, "\t", iva3, "\t\t", tot3)
print("-----------------------------------------")
print("Total a pagar: ", tot)
print("-----------------------------------------")