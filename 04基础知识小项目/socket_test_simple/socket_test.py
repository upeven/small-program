from socket import *

myHost = ''
myPort = 50007

sockobj = socket(AF_INET,SOCKE_STREAM)    # 创建socket.TCP实例
sockobj.bind(myHost,myPort)    #绑定主机与端口
sockobj.listen(5)      #监听程序，允许同时监听5个连接

while True:
    connection,address = sockobj.accept()
    print('Server connected by',address)
    while True:
        data = connection.recv(1024)
        if not data:break

        connection.send(b"Echo=>"+data)
    connection.close()
