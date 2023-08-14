#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
# venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso 
# de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso 
# pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.

dolls = int(input("numbers the dolls requested?: "))
clown = int(input("numbers the clowns requested?: "))

weigth_doll = 0.075
weigth_clown = 0.112

weigth_request = round(dolls*weigth_doll + clown*weigth_clown,2)

print(f"the wight  total of request is: {weigth_request}kg")