#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es 
#un número primo o no.

n = int(input("num: "))
i = 2
while n % 2 != 0:
    i += 1
if 3 == n:
    print("is prime")
else:
    print(" is not prime")