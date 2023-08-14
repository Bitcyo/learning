class Cars:
   def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model 
        self.year = year
        self.mileage = mileage
    
   def Info(self):
        print(f"""
              CAR DETAILS:
              Make: {self.make}
              Year: {self.year}
              model: {self.model}
              mileage: {self.mileage}     
              """)
      
input()     
car = Cars("Toyota" , "ak47", "2022", "2004")

car.Info()

