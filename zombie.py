"""
    僵尸进程
"""
import os
import signal
# 信号方法处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print('ERROR')
elif pid == 0:
    print('Child Process:',os.getpid())
    os._exit(1)
else:
    # p,status = os.wait()
    # print('PID:',p)
    # print('Status:',os.WEXITSTATUS(status))
    while True:
        pass





