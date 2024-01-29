#*************************** Opeater Overloding *******************
class book:
    def __init__(self,pages,):
        self.pages=pages
    def __add__(self, other):
        return self.pages + other.pages

b1=book(200)
b2=book(200)
b3=book(1200)
print(b1 + b2)

print('*'*20)


class books:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'The pages of books are:'+ str(self.pages)
b=books(200)
print(b)
print('*'*20)

class book:
    def __init__(self,pages,):
        self.pages=pages
    def __str__(self):
        return  'The number of pages are:'+str(self.pages)
    def __add__(self, other):
        total= self.pages + other.pages
        b=book(total)
        return b

b1=book(200)
b2=book(200)
b3=book(1200)
b4=book(200)
print(b1+b2+b3+b4)

class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks
    def __lt__(self, other):
       return self.marks<other.marks

s1=Student("bubay",200)
s2=Student("soumadeep",300)
print(s1<s2)
print(s2<s1)

print('*'*20)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self, other):
        return self.salary*other.days
class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
e=Employee('Bubay',500)
t=Timesheet('Bubay',30)
print('The Salary of this month is',e*t)






























