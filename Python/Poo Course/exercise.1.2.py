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

student = Student(name, yearsOld, grade)
print(f"""
    STUDENT INFO: \n\n
    name: {student.name}
    yearsOld:  {student.yearsOld}
    grade: {student.grade}     
      """)


while True:
    learning = input()
    if (learning.lower() == "learning"):
        student.learning()

