class Student:
    def __init__(self, name, yearsOld, grade):
        self.name = name
        self.yearsOld = yearsOld
        self.grade = grade
         
    def learning(self):
     print(f"{self.name} is studing rigth now")
     
     
name = input("whats your name?: ")
yearsOld = input("years old?: ")
grade = input("whats your grade?: ")

student_instance = Student(name, yearsOld, grade)
student_instance.learning()






        
         