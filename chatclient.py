"""
chat room 客户端
"""
from socket import *
import os,sys

# 服务端地址
ADDR = ('127.0.0.1',8888)

# 子进程发送消息
def send_msg(s,name):
    while True:
        try:
            text = input('发言：')
        except KeyboardInterrupt:
            text = 'quit'
        if text =='quit':
            msg = 'Q '+name
            s.sendto(msg.encode(),ADDR)
            sys.exit('退出聊天室')
        msg = 'C %s %s'%(name,text)
        s.sendto(msg.encode(),ADDR)
# 父进程接收消息
def recv_msg(s):
    while True:
        data,addr=s.recvfrom(4096)
        if data ==b'EXIT':
            sys.exit()
        print(data.decode()+'\n发言:',end='')

# 网络搭建
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    # 进入聊天室
    while True:
        name = input('请输入姓名')
        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        # 得到反馈
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print('请进入聊天室')
            break
        else:
            print(data.decode())

    # 创建进程
    pid = os.fork()
    if pid<0:
        print('Error')
    if pid == 0:
        send_msg(s,name)
    if pid > 0:
        recv_msg(s)

if __name__ == '__main__':
    main()


