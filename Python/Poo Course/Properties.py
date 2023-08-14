class People:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age
    @property   
    def name(self): 
        return self.__name 
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @name.deleter
    def name(self):
        del self.__name

Luis = People("Luis", 18)

name = Luis.name
print(name)

Luis.name = "Angel"

name = Luis.name
print(name)

del Luis.name



