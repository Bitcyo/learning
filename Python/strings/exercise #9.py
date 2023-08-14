#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior
# para que también funcione cuando el día o el mes se introduzcan con un solo carácter

born = input("born date (00/00/000): ")

date_born = born.split("/")

day  = date_born[0]
month  = date_born[1]
year = date_born[2]

print(f"dia: {day}\nmes: {month}\nyear: {year}")