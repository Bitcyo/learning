#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

rent = float(input("how much your anual rent: "))

if rent < 10000 :
    print("impositive: 5%")

elif rent > 10000 and rent < 20000:
    print("impositive: 15%")
elif rent > 20000 and rent < 35000 :
    print("impositive: 20%") 
elif rent < 35000 and rent < 45000:
    print("impositive: 30%")
else :
    print("impositive: 40%")