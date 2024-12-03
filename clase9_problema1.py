# Suma de números naturales

'''
Desarrolla un programa en Python que calcule la suma de los números naturales hasta un
número dado utilizando un bucle for. 

La suma de los números naturales hasta el número n se
define como la suma de todos los números enteros positivos desde 1 hasta n.

Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.

Tips:
● ¡Usá range()!
● El programa debe pedir un número entero n y devolver la suma de los números
naturales hasta n.

'''


n = int(input("ingrese numero natura n: "))
suma = 0
cadena = "1"
for numero in range(1,n+1):
    suma += numero
    if(numero != 1):
        cadena = cadena + "+" + str(numero)
print(f"{cadena} = {suma}")