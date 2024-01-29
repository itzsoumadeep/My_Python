import  sys
class Customer:
    '''Customer class with bank related operation'''

    bankname="GHOSH BANK" #--> static variable

    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print(f"After Deposit the balance: {self.balance} ")

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient balence... can not perform this operation ")
            sys.exit()
        self.balance=self.balance-amt
        print(f"After Withdraw the balance: {self.balance} ")

print(f"Welcome to {Customer.bankname} ")
name=input("Enter your name: ")
c=Customer(name)
while True:
    print("d- Deposit\nw- Withdraw \ne-Exit")
    option=input("Choose your option: ")
    if option=="d" or option=="D":
        amt=float(input("Enter amount to Deposit: "))
        c.deposit(amt)
    elif  option=="w" or option=="W":
        amt=float(input("Enter amount to Withdraw: "))
        c.withdraw(amt)
    elif option=="e" or option=="E":
        print("Thanks for Banking")
        sys.exit()
    else:
        print("Choose valid option")


