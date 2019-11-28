import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


def service_client(new_socket):
    request = new_socket.recv(1024)
    request = request.decode("utf-8")
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
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content.encode("utf-8"))
    except FileNotFoundError:
        response = "HTTP/1.1 404 FILENOTFOUND\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += "\r\n"
        response += "<h1>找不到文件</h1>"
        new_socket.send(response.encode("utf-8"))

    new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 8080))

    tcp_server_socket.listen(128)

    while True:
        new_socket, client_addr = tcp_server_socket.accept()

        gevent.spawn(service_client, new_socket)


if __name__ == '__main__':
    main()
