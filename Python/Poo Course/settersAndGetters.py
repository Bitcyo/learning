class People:
    def __init__(self, name, age):
        self._name = name 
        self._age = age
        
    def get_name(self): 
        return self._name #funcion para obtener valores
    
    def set_name(self, new_name):
        self._name = new_name #funcion para modificar valores
    
    
Luis = People("Luis", 18)

name = Luis.get_name()
print(name)

Luis.set_name("Angel")

name = Luis.get_name()
print(name)

        
        