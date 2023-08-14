#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
#Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

weigth = float(input(f"what is your weigth(kg)?: "))
high = float(input(f"what is your high(m)?: "))

IMC = weigth/(high**2)

result = round(IMC,2)

print(f"your IMC with weigth: {weigth}kg and high: {high}m is: {result}")