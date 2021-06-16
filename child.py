import os
from time import sleep
def f1():
    sleep(2)
    print('func01')
def f2():
    sleep(3)
    print('func02')
pid = os.fork()
if pid <0:
    print('Error')
elif pid ==0:
    if pid ==0:
        f1()
    else:
        os._exit(0)


