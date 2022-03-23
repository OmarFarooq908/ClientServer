import socket

host = '172.16.74.252'
port = 3458

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    print("Omar >> "+client.recv(1024).decode('utf-8'))
    message = input("Hassam >> ")
    message = "Hassam >> " + message
    client.send(message.encode('utf-8'))
