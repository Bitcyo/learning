class Phone:
    def __init__(self, camera, model,brand):
        self.camera = camera
        self.model = model
        self.brand = brand
        
    def call(self):
        print(f"calling in your {self.model}")
        
    def HandsUp(self):
        print(f"handUp in your {self.model}")
        
                
    
phone1 = Phone("48px","3310","brand")

print(phone1.call())
