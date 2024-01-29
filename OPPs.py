class Employee:
    '''this class crited by Soumadeep ghosh'''
    def __init__(self,eno,ename,esal,eadd,eage):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
        self.eage=eage

    def info(self):
        print(f"Employee no is {self.eno}")
        print(f"Employee name is {self.ename}")
        print(f"Employee salary is {self.esal}")
        print(f"Employee address is {self.eadd}")
        print(f"Employee age is {self.eage}")

e=Employee(8653980889,"Soumadeep",100000,"kolkata",20)

b=Employee(9734452307,"Bubay",50000,"newtown",30)
e.info()
print("-"*50)
b.info()
print(Employee.__doc__)
help(Employee)
print(id(Employee))
print(id(e))
print(id(b))


