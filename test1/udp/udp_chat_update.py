import socket


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    send_data = input("请输入发送内容:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7788))
    # dest_ip = input("请输入对方ip:")
    # dest_port = int(input("请输入对方端口："))
    dest_ip = "127.0.0.1"
    dest_port = 8080

    while True:
        print("--------聊天器-------")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        op = input("请输入功能代号：")
        if op == "1":
            send_msg(udp_socket, dest_ip, dest_port)
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误，请重新输入")
    udp_socket.close()


if __name__ == '__main__':
    main()
