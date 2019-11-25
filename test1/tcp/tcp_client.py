import socket


def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_ip = "127.0.0.1"
    dest_port = 8989

    server_addr = (dest_ip, dest_port)
    tcp_client_socket.connect(server_addr)

    while True:
        send_data = input("请输入发送的数据：")
        tcp_client_socket.send(send_data.encode("utf-8"))
        recv_data = tcp_client_socket.recv(1024)
        print(recv_data.decode("utf-8"))

    tcp_client_socket.close()


if __name__ == '__main__':
    main()
