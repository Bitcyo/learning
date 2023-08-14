#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
# el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir 
# un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el 
# grupo que le corresponde.

sex = input("women(W),man(M): ")
name = input("name: ")

initial = name[0].upper()

if  (sex == "W" and initial < "M") and (sex == "M" and initial > "M"):
    print("perteneces al grupo A ")
    
else:
    print("perteneces al grupo B")