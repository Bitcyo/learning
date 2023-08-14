#Escribir un programa que pida al usuario que introduzca una frase en la consola 
# y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
prhase = input("a prhase: ")
vocal = input("a vocal: ")

transform_vocal = prhase.replace(vocal,vocal.upper())

print(transform_vocal)

