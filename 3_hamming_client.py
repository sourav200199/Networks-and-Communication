import socket

host = socket.gethostname()
port = 5000

client = socket.socket()
client.connect((host, port))

msg = input("Enter msg to send: ")
client.send(msg.encode())

data = client.recv(1024).decode()
print("Hamming code: ", data)

client.close()