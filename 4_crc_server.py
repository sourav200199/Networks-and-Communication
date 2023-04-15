import socket

host = socket.gethostname()
port = 5000

server = socket.socket()
server.bind((host, port))
server.listen(2)

conn, addr = server.accept()

print(f"Connection successful from: {addr}")

def crc(msg, key):
    n2 = len(key)

    msg += '0' * (n2-1)
    msg = list(msg)
    key = list(key)
    n1 = len(msg)

    for i in range (n1-n2+1):
        if msg[i] == '1':
            for j in range(n2):
                msg[i+j] = str(int(msg[i+j]) ^ int(key[j]))

    return ''.join(msg[(-(n2-1)):])

data = conn.recv(1024).decode()
key = conn.recv(1024).decode()
rem = crc(str(data), str(key))

print(f"Remainder: {rem}")
msg = str(data) + rem
print(f"Codeword: {msg}")