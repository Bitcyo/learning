class People:
    def __init__(self, name, age, nacionality):
        self.name = name
        self.age = age
        self.nacionality = nacionality

class Artist:
    def __init__(self, skill):
        self.skill = skill
        
    def show_skill(self):
        print (f"My skill is {self.skill}")
    
        
class EmployeeArtist(People,Artist):
    def __init__(self, name, age, nacionality, skill, salary, company):
        People.__init__(self,name, age, nacionality)
        Artist.__init__(self,skill)
        self.salary = salary 
        self.comapany = company 
    
    def Present(self):
        print (f'hola soy {self.name}, my skill is {super().show_skill()} and working in {self.comapany}')
        
        
        
Luis = EmployeeArtist("luis", "18", "Perú", "play game", "$1000", "bitcyo.tm")

Luis.Present()    

heren = issubclass(EmployeeArtist,People)

instance = isinstance(Luis,EmployeeArtist)

print(heren,instance)