class Animal:
    def __init__(self,name):
        self.name = name

    def Eat(self):
        print(f"the {self.name} is  eating")
    
class Mammal(Animal):
    def __init__(self,name):
        Animal.__init__(self, name)
    
    def breastfeeding(self):
        print(f"the {self.name} is breastfeeding")
        
    
class Bird(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
        
    def fly(self):
        print(f"the {self.name} flying")
    
class Bat(Mammal, Bird):
    pass

bat  = Bat("bat luisito")

bat.Eat()
bat.breastfeeding()
bat.fly()