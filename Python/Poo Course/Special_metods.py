#metodos especiales pre definidos por  python

#__init__ constructor de clases

class People:
    def __init__(self, age, name):
        self.age = age
        self.name = name 

#__str__ representa los objetos en en strings, el programador debe establecer como quiere
#que se muestre la representación

    def __str__(self):
        return f"juas i'm {self.name} and have {self.age}" #esta es una represntacion mediocre de la clase persona

#__repr__   ofrece una represetaión mas detallada de lo sobjetos y sus elementos

    def __repr__(self):
        return f'"{self.age}", {self.name}'
#__add__ permite definir como queremos que se comporte la suma de 2 valores con los operadores 
    def __add__(self, other):
        new_value = self.age + other.age 
        return People(self.name+other.name,new_value)
    
Luis = People("Bitcyo", 18)

valentine = People("Val", 14)

new_person = Luis + valentine
print(new_person)
