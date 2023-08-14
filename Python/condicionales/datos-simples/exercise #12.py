#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después 
# el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pan = int(input("How many yesterday's loaves are there?: "))

price = 3.49
discount = price*0.6
total_with_discount = round(discount*pan)


print(f"the normally price is {price}, with 20% discount in {pan} loaves  the total is: {total_with_discount}")
