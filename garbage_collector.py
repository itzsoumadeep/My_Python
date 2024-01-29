import time
import gc
class Test:
    def __init__(self):
        print("Object initialization.................")

    def __del__(self):
        print("fullfiling last performation")

t1=Test()
t1=None
time.sleep(5)
print('End')
