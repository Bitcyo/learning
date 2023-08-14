class People:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def show_info(self):
        print(f"""
                name: {self.name}
                Years old: {self.age}
              """)
class Student(People):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def info_student(self):
        print(f"""
              {super().show_info()}
              student grade: {self.grade}
              """)
        
Luis = Student("luis", 18, "5to")

Luis.info_student()

