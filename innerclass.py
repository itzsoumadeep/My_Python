# class Outer:
#     def __init__(self):
#         print("outer class object")
#     def m2(self):
#         print("outer class method")
#     class Inner:
#         def __init__(self):
#             print("inner class object")
#         def m1(self):
#             print("inner class method")
# # o=Outer()
# # i=o.Inner()
# # i.m1()
# Outer().Inner().m1()
# Outer().m2()

# class Person:
#     def __init__(self,name,dd,mm,yyyy):
#         self.name=name
#         self.dob= self.DOB(dd,mm,yyyy)
#     def display(self):
#         print('Name', self.name)
#         self.dob.display()
#
#
#     class DOB:
#         def __init__(self,dd,mm,yyyy):
#             self.dd=dd
#             self.mm=mm
#             self.yyyy=yyyy
#         def display(self):
#             print(f" DOB is {self.dd}/{self.mm}/{self.yyyy}")
# p=Person("Bubay",8,5,2003)
# p.display()
#

# class human:
#     def __init__(self):
#         self.name='bubay'
#         self.head=self.Head()
#     def display(self):
#         print('Name',self.name)
#         self.head.talk()
#         self.head.brain.think()
#
#
#
#     class Head:
#         def __init__(self):
#             self.brain=self.Brain()
#
#         def talk(self):
#             print("talking............")
#
#         class Brain:
#             def think(self):
#                 print("Thinking............")
#
#
# h=human()
# h.display()
#
#





