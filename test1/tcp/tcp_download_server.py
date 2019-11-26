import socket


def send_file_2_client(client_socket):
    file_name = client_socket.recv(1024).decode("utf-8")
    print("客户端请求下载文件名：" + str(file_name))

    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read(1024)
        f.close()
    except FileNotFoundError as ret:
        print("没有要下载的文件" + file_name + " " + str(ret))

    if file_content:
        client_socket.send(file_content)


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)

    while True:
        client_socket, client_addr = tcp_server_socket.accept()
        send_file_2_client(client_socket)

        client_socket.close()
        
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
