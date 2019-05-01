import socket
import threading

def send_tcp(cnc_ip = '127.0.0.1', cnc_port = 8000, send_data = "01"):
    # 1.创建套接字socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.连接服务器
    #cnc_ip = input("请输入服务器ip：")
    #cnc_port = int(input("请输入服务器port："))
    cnc_addr = (cnc_ip, cnc_port)
    tcp_socket.connect(cnc_addr)

    # 3. 接收/发送数据
    #send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode())    
    
    # 接收服务器发送的数据
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode())    

    # 4. 关闭套接字socket
    tcp_socket.close()
    return

def get_cnc_command(client, address):
    try:
    #设置超时时间
        client.settimeout(500)
    #接收数据的大小
        buf = client.recv(2048)
    #################处理数据##############
        print("接收到的数据：%s" % buf.decode())
    #超时后显示退出
    except socket.timeout:
        print('time out')
    #关闭与客户端的连接
    client.close()

def recieve_tcp(cnc_ip = '127.0.0.1', cnc_port = 8000):
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
     # 2.绑定端口
    addr = (cnc_ip, cnc_port)
    tcp_server_socket.bind(addr)

    # 3.监听链接
    tcp_server_socket.listen(128)
    while(True):
        # 4.接收别人的连接
        # client_socket用来为这个客户端服务
        client_socket, client_addr = tcp_server_socket.accept() 
        # 5.接收对方发送的数据
        thread = threading.Thread(target=get_cnc_command,args = (client_socket, client_addr))
        thread.start()

    # 7.关闭套接字 
    #client_socket.close()
    #tcp_server_socket.close()

def main():
    cnc_ip = input("请输入服务器ip：")
    cnc_port = int(input("请输入服务器port："))
    while(1):
        send_data = input("请输入要发送的数据：")
        if(send_data==''):
            break
        send_tcp(cnc_ip,cnc_port,send_data)
    #recieve_tcp(cnc_ip,cnc_port)



if __name__ == "__main__":

        main()