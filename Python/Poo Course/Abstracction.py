class Auto():
    def __init__(self):
        self.status = "of"
        
    def On(self):
        self.status = "on"
        print("run run")

    def Drive(self):
        if self.status == "of":
            self.On()
            print("starting")

            
BWM = Auto()

BWM.Drive()
            