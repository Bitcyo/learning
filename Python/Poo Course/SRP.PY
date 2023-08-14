#SRP -principio de responsabilidad unica, Un princiipio que establece que Una clases se dedique
# a una unica respondabilidad, evitando conflictos con otras responsabilidades en caso de que la
#clase comparta mas responsabilidades

class FuelTank:
    def __init__(self):
        self.fuel = 100
        
    def add_fuel(self,amount):
         self.fuel += amount        
    
    def get_fuel(self):
          return self.fuel
      
    def use_fuel(self, amount):
        self.fuel -= amount
        
    def get_position(self):
        return self.position

class Car():
    def __init__(self,tank):
        self.position = 0
        self.tank = tank
        
    def move(self, distance):
        if self.tank.get_fuel() >= distance / 2:
            self.position += distance
            self.tank.use_fuel -= distance / 2
            
        else:
            print("fuel no enugh")
            

tank = FuelTank()
run_run = Car(tank)

             
     