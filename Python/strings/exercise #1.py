#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

name  = input("whats your name: ")

num = int(input("insert a num: "))

name_multiplicate = (name+"\n") * num

print(name_multiplicate)