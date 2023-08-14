#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

C = float(input("what is your invertion: ")) #capital
i= float(input("interest?: ")) #interest
t = float(input("what is the years de invertion?: ")) #time

invesment_result = C*(i/100)*t

print(f"your invesment from {C}$ to {i}% in {t} years you get {invesment_result}$")