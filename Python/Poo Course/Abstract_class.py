from abc import ABC, abstractclassmethod

class People(ABC):
    @abstractclassmethod
    def __init__(self, name, age, sex, activity):
        self.name = name 
        self.age = age
        self.sex = sex
        self.activity = activity
    
    @abstractclassmethod
    def Activity(self):
        pass
    
    def Presentation(self):
        print(f"Hi, i'm {self.name} and have {self.age} years old")
        
class Student(People):
    def __init__(self, name, age, sex, activity):
        super().__init__(name, age, sex, activity)
        
    def Activity(self):
        print(f"I'm doing {self.activity}")
        
Bitcyo = Student("Luis", 18, "a veces...casi nunca...bue..no :(", "hacking")

Bitcyo.Activity()