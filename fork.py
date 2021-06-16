"""
修改了
"""
import os
import time
print('===============')
a =1
pid = os.fork()
if pid < 0:
    print('create process failed')
elif pid == 0:
    # time.sleep(3)
    print('this is new process')
    print('a=',a)
    a = 10000
else:
    time.sleep(1)
    print('this is old process')
    print('a=', a)





