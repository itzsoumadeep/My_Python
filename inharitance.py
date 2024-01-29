class p:
    def property(self):
        print('Cash+House+Gold+Power')
    def marrege(self):
        print('XYZ')
class c(p):
    def marrege(self):
        # super().marrege()

        print('PQR')
b=c()
b.property()
b.marrege()
print('*'*20)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(person):
    def __init__(self,name,age,empno,empsal):
        super().__init__(name,age)
        self.empno=empno
        self.empsal=empsal

    def display(self):
        print('Employee name: ',self.name)
        print(f"Employee age: {self.age}")
        print(f"Employee Number: {self.empno}")
        print(f"Employee Salary: {self.empsal}")
e1=Employee('Bubay',20,77,71)
e1.display()

print('-'*30)


#***************** Single Inharitance *******************

class P: # --> Parent class
    def m1(self):#-->m1 contained 1 argument
        print('Parent Method...........')
class C(P): # --> Child class
    def m2(self):#-->m2 contained 2 argument
        print('child Method.............')
c=C()
c.m1()
c.m2()
print('-'*30)

#***************** Multiple Inharitance *******************

class P: # --> Parent class
    def m1(self):#-->m1 contained 1 argument
        print('Parent Method...........')
class C(P): # --> Child class
    def m2(self):#-->m2 contained 2 argument
        print('child Method.............')
class CC(C):
    def m3(self):#-->m3 contained 3 argument
        print('Subchild method.........')
c=CC()
c.m1()
c.m2()
c.m3()
print('-'*30)

#***************** Hierarchical Inharitance *******************

class P: # --> Parent class
    def m1(self):#-->m1 contained 1 argument
        print('Parent Method...........')
class C1(P): # --> Child class
    def m2(self):#-->m2 contained 2 argument
        print('child1 Method.............')
class C2(P):
    def m3(self):#-->m3 contained 3 argument
        print('child2 method.........')
c=C1()
c.m1()
c.m2()
d=C2()
d.m1()
d.m3()

print('-'*30)

#***************** Multiple Inharitance *******************

class P1: # --> First parent class
    def m1(self):
        print('Parent1 Method..')
class P2: # -->Second Parent class
    def m1(self):
        print('Parent2 method.........')

class C(P2,P1): # P2 class will be execute first because in class C P2 is first
    pass
c=C()
c.m1()

#***************** Hybrid Inharitance *******************

# class A:
#     def m1(self):
#         print('A class Method')
# class B(A):
#     def m1(self):
#         print('B class method')
# class C(A):
#     def m1(self):
#         print('C class method')
# class D(B,C):
#     def m1(self):
#         print('D class method')




class a:
    pass
class b:
    pass
class c:
    pass
class x(a,b):
    pass
class y(b,c):
    pass
class p(x,y,c):
    pass
print(p.mro())


















