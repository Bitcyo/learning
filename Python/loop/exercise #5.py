#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
invesment = float(input("invesment: "))
interest = float(input("interest: "))
years = int(input("years: "))


for i in range(1,years+1):
    gana = (invesment*(1+ (interest/100))**i)-invesment
    print(f"en el año {i} tienes: {gana}$ ")