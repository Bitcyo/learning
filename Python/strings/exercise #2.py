#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces,
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

name = input("what is your name?: ")

name_minisculas = name.lower() 
name_mayusculas = name.upper()
name_correcto = name.capitalize()

print(f"primera forma: {name_minisculas}\nsegunda forma: {name_mayusculas}\n tercera forma: {name_correcto}\n si no escribiste tu nombre de ningunas de estas formas eres tremendo gil")
