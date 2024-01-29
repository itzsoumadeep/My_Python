class Person:
    def __init__(self,name,age):
            self.name=name
            self.age=age
    def display(self):
        print('Name',self.name)
        print('age',self.age)

class Student(Person):
    def __init__(self,name,age,roll,marks):
        super().__init__(name,age)#--> Don't need to write self.name or self.age or whatever you written in Parent class
        self.roll=roll
        self.marks=marks
    def m1(self):
        super().display()#-->Print of name & age written in Person class.Using super dont need to reprint
        print('Roll No: ',self.roll)
        print('Marks: ',self.marks)

class Techer(Person):
    def __init__(self,name,age,salary,subject):
        super().__init__(name,age)#--> Don't need to write self.name or self.age or whatever you written in Parent class
        self.salary=salary
        self.subject=subject

    def m2(self):
        super().display()#-->Print of name & age written in Person class.Using super dont need to reprint
        print('Salary: ', self.salary)
        print('Subject: ', self.subject)
s=Student('Bubay',20,71,00)
s.m1()
t=Techer('Soumadeep',55,500000,'Python')
t.m2()


'''How to call perticular parent class method by using super()'''
#1. parent_classname.method_name(self)

class A:
    def m1(self):
        print('A class Method...........')
class B(A):
    def m1(self):
        print('B class Method.............')
class C(B):
    def m1(self):
        print('C class method.........')
class D(C):
    def m1(self):
        print('D class method.........')
class E(D):
    def m1(self):
        B.m1(self)#--> Call particular method
e=E()
e.m1()
print('*'*30)

#2.super(class_name,self).method_name()

class A:
    def m1(self):
        print('A class Method...........')
class B(A):
    def m1(self):
        print('B class Method.............')
class C(B):
    def m1(self):
        print('C class method.........')
class D(C):
    def m1(self):
        print('D class method.........')
class E(D):
    def m1(self):
        super(C, self).m1()#--> Super of C class willbe called means B will be called
e=E()
e.m1()
print('*'*30)


class P:
    def __init__(self):
        print('Parent constructor')
    def m1(self):
        print('Parent instant method')
    @classmethod
    def m2(cls):
        print('parent class method')
    @staticmethod
    def m3 ():
        print('parent static method')
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c=C()





















