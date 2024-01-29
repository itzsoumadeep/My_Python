class Student:
    collegeName='TIB'

    def __init__(self,name):
        self.name=name

    def display(self):
        print(f"Student name: {self.name} and college name: {Student.collegeName}")

s=Student('Bubay')
s.display()