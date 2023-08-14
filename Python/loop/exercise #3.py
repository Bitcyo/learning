#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = int(input("insert a num: "))

for i in range(num):
    if i % 2 == 0:
        print(f"{i} es par",end =(", "))
    else:
        print(f"{i} impar",end =(", "))