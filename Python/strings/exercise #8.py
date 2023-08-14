#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
# muestre por pantalla el número de euros y el número de céntimos del precio introducido.

price = input("insert price product(two deciimals,use a point): ")

price_decimal = price.split(".")

inter = price_decimal[0]
float = price_decimal[1]

print(f"you have {inter}$ with {float}")