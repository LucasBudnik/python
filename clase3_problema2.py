# Calculadora de propinas

#Escribe un programa en Python que calcule la
#propina que se debe dejar en un restaurante.

#El script debe solicitar al usuario el monto total de
#la cuenta y el porcentaje de propina que desea
#dejar.
monto_total_de_la_cuenta = float(input("ingrese monto total de la cuenta: "))
porcentaje_propina = int(input("ingrese porcentaje de propina: "))


#Utilizando operadores aritméticos, calcula la
#cantidad de propina y el total a pagar (incluyendo
#la propina).
propina = (monto_total_de_la_cuenta * porcentaje_propina) / 100
total_a_pagar = monto_total_de_la_cuenta + propina

#Finalmente, muestra los resultados en la pantalla.

print(f"El monto de la cuenta es de {monto_total_de_la_cuenta}$")
print(f"El porcentaje de la propina es de {porcentaje_propina} %")
print(f"La propina es de {propina}$")
print(f"El total a pagar es de {total_a_pagar}$")
