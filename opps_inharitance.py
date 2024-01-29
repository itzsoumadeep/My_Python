
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id


    def Showdetails(self):
        print(f"The name of the Employee is {self.name} id {self.id}")


class Developer(Employee):
    def showLanguage(self):
        print(f"The most preferlable language is python")



e1=Employee("Bubay",17)
e1.Showdetails()

e2=Developer("Soumadeep Ghosh",6544566)
print(e2.__dir__())

e2.showLanguage()