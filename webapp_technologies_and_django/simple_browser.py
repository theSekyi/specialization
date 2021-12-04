import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(("https://www.esekyi.com/", 80))
cmd = "GET https://www.esekyi.com HTTP/1.1\r\n\r\n".ecode()

my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

my_socket.close()
