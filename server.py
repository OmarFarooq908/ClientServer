import socket

host = '172.16.74.252'
port = 3458

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(5)
x = True
communication_socket, address = server.accept()
while True:
    if (x):
        print(f"Connected to {address}")
    x = False
    write = input("Omar >> ")
    message = communication_socket.send(write.encode('utf-8'))
    print(communication_socket.recv(1024).decode('utf-8'))

