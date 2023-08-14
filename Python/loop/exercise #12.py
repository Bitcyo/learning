#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

prahse = input("write a prhase: ") 
letter = input(" chose leterr: ")
count = 0 
for i in prahse:
    if i == letter:
        count += 1
print(count)       
    
