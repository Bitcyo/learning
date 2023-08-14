#Escribir un programa que pregunte el correo electrónico del usuario en la consola 
# y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante 
# de la arroba @) pero con dominio ceu.es.
mail = input("give your e-mail: ")

replace = mail.replace("gmail","ceu.es")

print(f"your new mail is: {replace}")