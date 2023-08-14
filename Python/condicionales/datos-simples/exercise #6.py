#Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta  n . La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma:
number = input("insert your number: ")

n = int(number)

result = n*(n+1)/2

print(f"the sum from 1 at {n} is: {result}")
