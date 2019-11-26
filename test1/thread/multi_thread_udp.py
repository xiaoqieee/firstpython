import socket
import threading


def recv_msg(udp_socket):
    """接收数据"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket):
    """发送数据"""
    while True:
        send_data = input("请输入要发送的内容：")
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 8080))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 8989))

    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket,))
    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()
