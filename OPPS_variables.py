#   class Student:
# #     def __init__(self):
# #         self.name="Soumadeep"
# #         self.roll=100
# #         self.idno=5
# #
# #
# #
# # e=Student()
# # print(e.__dict_)




# ******************* Instant variable *************

'''class student:
    def __init__(self,name,roll,section,backlog_sub,passed_sub):
        self.name=name # -->Inside constructure instant veriable declare
        self.roll=roll
        self.section=section
        self.backlog_sub=backlog_sub
        self.passed_sub=passed_sub

    def info(self):
        self.marks=100 # -->Inside instant method instant veriable declare

    def display(self):
        print(f"My name is {self.name}") # --> access Instance variables

    def deletevariable(self):
        del self.backlog_sub,self.passed_sub # --> delete instance variable Within a class

s= student("Bubay",71,"A",2,3)
s.age=18  # --> Outside of the class instant veriable declare
s.deletevariable()
print(s.__dict__)
print(s.section) # --> access instance variables outside of the class
s.display()

s1=student("Soumadeep",33200121071,"B",4,1)
del s1.section  # --> delete instance variable From outside
print(s1.__dict__)
s1.display()




# ******************* Static variable *************


class student:
    colege_name="TIB"  # --> Static variable declaring e within the class directly but from out side of any method.

    def __init__(self, name, roll, section):
        self.name=name
        self.roll=roll
        self.section=section

    def addr(self):
        student.address="Goaltore" #--> Static variable declaring Inside instance method by using class name


    @classmethod
    def marks(cls):
        cls.highmarks=99  #--> Inside classmethod by using  cls  static variable declaring & access
        student.lowmarks=40 #--> inside classmethod using class name Static variable declaring & access


    @staticmethod
    def school_name():
        student.school_name="Goaltore High school" #-->Inside static method by using class name

student.gf="single" #--> static variable declearing outside the class
s1=student("Bubay",71,"A")
s2=student("Soumadeep",33200121071,"B")
s1.marks()
s2.marks()
s1.addr()
s2.addr()
print(student.__dict__)
print(s1.name,s1.roll,s1.section)
print(s1.colege_name)
print(s1.addr())
print(s2.name,s2.roll,s2.section)
print(s2.colege_name)

#  **************Access static variable***********

class Test:
    math=90

    def __init__(self):
        print(self.math) #--> Inside constructor: by using either self
        print(Test.math) #-->                              or classname

    def ex1(self):
        print(self.math) #--> inside instance method: by using either self
        print(Test.math) #-->                                  or classname
    @classmethod
    def ex2(cls):
        print(cls.math) #-->inside class method: by using either cls variable
        print(Test.math) #-->                                  or classname
    @staticmethod
    def ex3(): #--> Inside static mathod : by useing class name
        print(Test.math)

t=Test()
print(Test.math) #From outside of class: by using either  classnmae
print(t.math)#-->                                or object reference
t.ex1()
t.ex2()
t.ex3()

#************************* Modify Static Veriable ********************


class Test:
    a=999
    @classmethod
    def m1(cls):
        cls.a=555
    @staticmethod
    def m2():
        Test.a=111
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)

#****************************** Delete Static Variable*******************

class Test:
    a=10
    def __init__(self):
        del Test.a
print(Test.__dict__)
print("-------------------------------------------")
t= Test()
print(Test.__dict__)'''

''' ********************** LOCAL VARIABLE **************
                        __________________             '''



class marks:
    def average(self,list):
        result=sum(list)/len(list)
        print(f"The Average of marks is: {result}")

m=marks ()
m.average([44,5,66,4])


