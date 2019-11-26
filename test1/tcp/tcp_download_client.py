import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(("127.0.0.1", 8080))
    file_name = input("请输入要下载的文件:")
    tcp_socket.send(file_name.encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    if recv_data:
        with open("[新]" + file_name, "wb") as f:
            f.write(recv_data)
    tcp_socket.close()


if __name__ == '__main__':
    main()
