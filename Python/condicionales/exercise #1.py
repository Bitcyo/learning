#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es
# mayor de edad o no.

edad = int(input("years old?: "))

if edad >= 18:
    print("a pagar impuestos")
else:
    print("a terminar la secundaria")