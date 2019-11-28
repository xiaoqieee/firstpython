import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 8080))

    tcp_server_socket.listen(128)

    tcp_server_socket.setblocking(False)

    client_socket_list = list()

    while True:
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as e:
            # print("-------没有新连接--------")
            pass
        else:
            print("-------监听到新连接--------")
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as e:
                pass
            else:
                if not recv_data:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                else:
                    print(recv_data.decode("gbk"))


if __name__ == '__main__':
    main()
