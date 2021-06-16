import os
from time import sleep
pid = os.fork()
if pid < 0:
    print('Error')
elif pid ==0:
    sleep(1)
    print('Child PID:',os.getpid())
    print('get Parent pid:',os.getppid())
else:
    print('Parent PID:',os.getpid())
    print('get child pid',pid)





