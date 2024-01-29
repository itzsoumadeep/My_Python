# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(f"Your name is: {self.name}")
#         print(f"your marks is: {self.marks}")
#
#     def grade(self):
#         if self.marks>=90:
#             print(f"your marks {self.marks} and your grade is O")
#         elif self.marks>=80:
#             print(f"your marks is {self.marks} and your grade is A")
#         elif self.marks>=70:
#             print(f"your marks is {self.marks} and your grade is B")
#         elif self.marks>=60:
#             print(f"your marks is {self.marks} and your grade is C")
#         elif self.marks>=50:
#             print(f"your marks is {self.marks} and your grade is D")
#         else:
#             print(print(f"your marks is {self.marks} and your are faild better luck next time"))
# n=int(input("Enter number of students:"))
#
# name=input("Enter student name: ")
# marks=int(input("Enter student marks: "))
# print("under ",n," number of student")
# s=Student(name,marks)
# s.display()
# s.grade()
# print("-"*30)

# ************************ Static method ********************
# class Studen:
#     @staticmethod
#     def add(x,y):
#         print(f"the sum is {x+y}")
#     @staticmethod
#     def product(x,y):
#         print(f"the sum is {x*y}")
# Studen.add(10,60)
# Studen.productC

class Employee:

    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename = ename
        self.esal=esal

    def display(self):
        print('Employee number is', self.eno)
        print('Employee name is',self.ename)

        print('Employee salary is',self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+100
        emp.display()
e=Employee(55555555,'bubay',7000)
Test.modify(e)

