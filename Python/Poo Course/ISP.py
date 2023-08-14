#ISP, consiste en fracionar una clase  base para que los metodos abstractos se puedan acoplar correctamente
#a exepciones a la regla general (en este caso un trabajador come,trabaja y duerme pero un robot solo come)
#al fracccionar la clase evitar conflictos

from abc import ABC, abstractmethod

class Worker(ABC):
    
   @abstractmethod
   def Work(self):
       pass
   
class Eater(ABC):
   
   @abstractmethod
   def Eat(self):
       pass
class Sleeper(ABC):
    
   @abstractmethod
   def Sleep(self):
       pass 
   
class Human(Worker,Eater,Sleeper):
    
   def Work(self): 
       print("working")
   
   def Eat(self):
       print("eating")

   def Sleep(self):
       print("sleeping")
       
class Robot(Worker):
    
   def Work(self):
       print("workking")
   
   
luis = Human()
bitcyo = Robot()
