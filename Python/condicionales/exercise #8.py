#el ejercicip esta muy largo como pars ponerlo aqui,algo de calcular los bonos con unos ppuntos 
#que los trabajadores ganaban en su empresa

puntos = float(input("How many points do you have: "))

bono = 2400.00

inacepted = 0.0

acepted = 0.4

merit = 0.6

if puntos == inacepted:
    print(f"no acepted")
elif puntos == acepted:
    print(f"acepted: {acepted*bono}" )
elif puntos >= merit:
    print(f"oh,is good: {merit*bono}")
else:
    ("only 0.0, 0.4 and 0.6 more ") 