import socket
import time

HOST = '127.0.0.1'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    client_socket.send(b'Hello world')
    time.sleep(5)
    data = client_socket.recv(1024)
    print(data)
