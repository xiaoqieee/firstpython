import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 8989))

    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的链接...")
        tcp_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)
        while True:
            recv_data = tcp_socket.recv(1024)
            if not recv_data:
                break
            print(recv_data.decode("utf-8"))
            tcp_socket.send("hahahah----ok-----".encode("utf-8"))
        tcp_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
