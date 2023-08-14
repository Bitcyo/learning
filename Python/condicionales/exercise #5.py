#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
# ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input("years old: "))
pay = int(input("pay ($): "))

if age >= 16 and pay >= 1000:
    print("you are a tributer citizen")
else:
    print("not atribute")
    
    