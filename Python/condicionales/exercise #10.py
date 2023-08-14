#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
pedido = input("pizza vegetariana?(y/n): ")
Ingredientes_vegetarianos = ["Pimiento", "tofu"]
Ingredientes_no_vegetarianos = ["Peperoni", "Jamón " "Salmón"]

if pedido == "y":
    print(f"los ingredientes son {Ingredientes_vegetarianos}")
elif pedido == "n":
    print(f"los ingredientes {Ingredientes_no_vegetarianos}")
else:
    print("error: introduce a answer correct")
