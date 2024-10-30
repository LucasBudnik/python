# OPERACIONES BASICAS

#Crea un programa que solicite al usuario dos
#números enteros.
num1 = int(input("Ingrese numero entero 1: "))
num2 = int(input("Ingrese numero entero 2: "))


#Realiza las siguientes operaciones: suma,
#resta, multiplicación, y módulo.
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

#Muestra el resultado de cada operación en un
#formato claro y amigable.

print(f"{num1} + {num2} = ",suma)
print(f"{num1} - {num2} = ",resta)
print(f"{num1} * {num2} = ",multiplicacion)
print(f"{num1} / {num2} = ",division)

#Asegúrate de incluir mensajes personalizados que
#expliquen cada resultado, por ejemplo: "La suma
#de tus números es: X".