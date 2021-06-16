import os
from time import sleep
def func01():
    sleep(2)
    print('func01 over')
def func02():
    sleep(3)
    print('func02 over')

pid = os.fork()
if pid <0:
    print('Error')
elif pid ==0:
    func01()
else:
    func02()


