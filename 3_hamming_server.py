import socket

host = socket.gethostname()
port = 5000

server = socket.socket()
server.bind((host, port))
server.listen(2)
conn, addr = server.accept()

print("Connection successful from client: ",addr)

data1 = conn.recv(1024).decode()
data1 = list(data1)
data1 = [int(i) for i in data1]
num = len(data1)
code = []

def check_parity(data, start, end):
    parity = 0
    for i in range(start, end, 2**(start+1)):
        for j in range(i, i+2**start):
            if j < end:
                parity += data[j]

    return parity % 2

def find_r(num):
    r = 0
    while(2**r < num + r + 1):
        r += 1

    return r

def hamming(data, num):
    r = find_r(num)
    n = num + r
    m = 0
    j = 0

    for i in range(1, n+1):
        if i == 2**m and m<=r:
            code.insert(i-1, 0)
            m += 1
        else:
            code.insert(i-1, data[j])
            j += 1

    m = 0
    for i in range(1, n+1):
        if i == 2**m and m<=r:
            code[i-1] = check_parity(code, i-1, n)
            m += 1

    return code

code1 = str(hamming(data1, num))

#Convert code1 to string and send
conn.send(code1.encode())

conn.close()

