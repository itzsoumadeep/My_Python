class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return  self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n=int(input("Enter number of students:"))

name=input("Enter student name: ")
marks=int(input("Enter student marks: "))

s=Student()
s.setName("Bubay")
s.setMarks(66)

print("Hiii",s.getName(),"Your marks is ",s.getMarks())

