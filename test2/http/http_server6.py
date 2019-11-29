import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


def service_client(new_socket, request):
    request_lines = request.splitlines()
    # print(request_lines)

    if len(request_lines) > 0:
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)

    print(file_name)
    if file_name == "/":
        file_name = "/index.html"

    try:
        f = open("../../web" + file_name)
        response_body = f.read().encode("utf-8")
        f.close()
        response_header = "HTTP/1.1 200 OK\r\n"
    except FileNotFoundError:
        response_header = "HTTP/1.1 404 FILENOTFOUND\r\n"
        response_body = "<h1>找不到文件</h1>".encode("utf-8")

    response_header += "Content-Length: %d\r\n" % (len(response_body))
    response_header += "Content-Type: text/html; charset=utf-8\r\n"
    response_header += "\r\n"
    new_socket.send(response_header.encode("utf-8"))
    new_socket.send(response_body)

    # new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 8080))

    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字改为非阻塞

    client_socket_list = list()

    while True:
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as e:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as e:
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data.decode("gbk"))
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)


if __name__ == '__main__':
    main()
