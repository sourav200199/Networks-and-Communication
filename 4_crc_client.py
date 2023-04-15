import socket

host = socket.gethostname()
port = 5000

client = socket.socket()
client.connect((host, port))

client.send((input("Enter message: ")).encode())
client.send((input("Enter key: ")).encode())