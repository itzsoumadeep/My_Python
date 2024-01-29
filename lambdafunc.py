# def double(x):
#     return x*2


#**************** Lambda Function **********
double=lambda x:x*2
print(double(5))


#******************* Use Case ******************

def sd(func,value):
    return 9+func(value)
# cube=lambda x:x*x*x
print(sd(lambda x:x*x*x,2))
