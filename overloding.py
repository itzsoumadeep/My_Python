#*************** Method Overloding ******************
class test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The sum is',total)
t=test()
t.sum(10,20)

class Test:
    def m1(self):
        print('No argument metthod')

    def m1(self,a):
        print('One argument metthod')

    def m1(self,a,b):
        print('Two argument metthod')

    def m1(self,a,b,c):
         print('Three argument metthod')
t=Test()
# t.m1(10)
# t.m1(10,20)
t.m1(10,20,30)

#*************** Constructor Overloding ******************
class Test:
    def __init__(self):
        print('No-Arg')
    def __init__(self,a):
            print('One-Arg')
    def __init__(self,a,b):
            print('two-Arg')
    def __init__(self,a,b,c):
        print('Three-Arg')
t1=Test(10,20,30)


class test:
    def __init__(self,a=None,b=None,c=None):
        print('Constructor with 0|1|2|3 number argument')
t1=test()
t1=test(10)
t1=test(10,20)
t1=test(10,20,30)












