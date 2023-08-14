#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente 
# <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente

n = int(input("insert num for divide: "))
m = int(input("insert a number with which to divide: "))

c = n/m

r = n%m

if r == 0:
  print(f"your numbers is:{n} divide by:{m}\n the result is: {c}\n and no have rest ({0}) ")
else:
 print(f"your numbers is:{n} divide by :{m}\n the result is: {c}\n and the rest is: {r}")