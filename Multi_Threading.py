'''Thread
    1.An independent part of a program.
    1.A flow of execution is concidered as thread.
    3.It's a python object.
    * For every thred an independent job is avalible'''


## Modul--> Threding

'''There is two way to import threading module
    1. import threading 
    2.from threading import *
          --> bigest advantage of 2nd one is calling any functuon we are not requird 
#                module name'''
#Functional  way
# from  threading import *
# def display():
#     for i in range(10):
#         print('Child thread' )
#
# t=Thread(target=display)#-->Creaction of thread object
# t.start()#-->Starting the thread
# for i in range(10):
#     print('main thread ')
#
#
# print('*'*30)
# #Object oriented way
# from  threading import *
# class MyThread(Thread):
#     def run(self): # The mathod run fixed
#         for i in range (10):
#             print( 'Child thread')
# t=MyThread()
# t.start()
# for i in range(10):
#     print('Main thread')
#
# print('*'*30)
#
#
#
# from  threading import *
# class Test:
#     def m1(self):
#         for i in range(10):
#             print('Child thread-1')
#
# obj=Test()
# t =Thread(target=obj.m1)
# t.start()
# for i in range(10):
#     print('Main thread-1')
# print('*'*50)
#
# #Without using multithreading and in output look the time
# import time
# def double(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('Double value: ',2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('Squre value: ',n*n)
# numbers=[1,2,3,5]
# begintime=time.time()
# squares(numbers)
# double(numbers)
# endtime=time.time()
# print('The total time taken: ',endtime-begintime)
# print('*'*50)
#
#
#
# #With using multithreading and in output look the time
# from threading import *
# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:",2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:", n * n)
# numbers = [1, 2, 3, 4, 5, 6]
# begintime = time.time()
# t1 = Thread(target=doubles, args=(numbers,))
# t2 = Thread(target=squares, args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("The total time taken:", time.time() - begintime)
#

# print('*'*50)

#
# from threading import *
# print(current_thread().getName())
# current_thread().setName("bubay")
# # print(current_thread().getName())
# print(current_thread().name)
#
#
# print('*'*50)


#Thread Identification number :
# from threading import *
# def test():
#     print('child thread')
# t=Thread(target=test())
# t.start()
# print('Main thread identification number: ',current_thread().ident)
# print('Child thread identification number: ',t.ident)

#active_count():
# from  threading import  *
# import time
# def display():
#     print(current_thread().name,'.......Started')
#     time.sleep(3)
#     print(current_thread().name,'......Ended')
# print('The number of active thread: ',active_count())
# t1=Thread(target=display(),name='Child-1')
# t2=Thread(target=display(),name='Child-2')
# t3=Thread(target=display(),name='Child-3')
# t1.start()
# t2.start()
# t3.start()
# print('The number of active thread: ',active_count())
# time.sleep(5)
# print("The Number of active Threads:", active_count())

# enumerate() function:


# from  threading import  *
# import time
# def display():
#     print(current_thread().name,'.......Started')
#     time.sleep(1)
#     print(current_thread().name,'......Ended')
# print('The number of active thread: ',active_count())
# t1=Thread(target=display(),name='Child-1')
# t2=Thread(target=display(),name='Child-2')
# t3=Thread(target=display(),name='Child-3')
# t1.start()
# t2.start()
# t3.start()
#
# l=enumerate()
# for t in l:
#     print('Thread name:',t.name)
#     print('Thread identification nymber:',t.ident)
#     print()
#     time.sleep(5)
#


'''join() method:
    if a thread wants to wait untill completing some other thread then we should go
    for join method..'''

from  threading import *
import  time
def display():
    for i in range(10):
        print('Bubay Thread')
        time.sleep(2)
t=Thread(target=display)
t.start()

t.join()
for i in range(10):
    print('Soumadeep Thread')


