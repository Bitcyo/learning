#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
years = int(input("whats years old: "))


for i in range(years):
    i += 1 
    print(f"haz cumplido: {i}years")
