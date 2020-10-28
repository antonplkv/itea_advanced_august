import socket

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(10)


while True:
    conn, addr = s.accept()

    while True:
        data = conn.recv(1024)

        if not data:
            break
        print(data)
        conn.send(data[::-1])