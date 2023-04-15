import socket

k = 8
# -------- Function to find the checksum of message --------

def findChecksum(msg, k):
    # Dividing sent message in packets of k bits.
    c1 = msg[ 0 : k]
    c2 = msg[ k : 2 * k]
    c3 = msg[2 * k : 3 * k]
    c4 = msg[3 * k : 4 * k]
    # Calculating the binary sum of packets
    Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]
 
    # Adding the overflow bits
    if(len(Sum) > k):
        x = len(Sum)-k
        Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
    if(len(Sum) < k):
        Sum = '0'*(k-len(Sum))+Sum
 
    # Calculating the complement of sum
    Checksum = ''
    for i in Sum:
        if(i == '1'):
            Checksum += '0'
        else:
            Checksum += '1'
    return Checksum

# -------- Main Function --------

host = socket.gethostname()
port = 5000 

server_socket = socket.socket() 
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept() 
print("Connection from: " + str(address))

data1 = conn.recv(1024).decode()
Checksum = findChecksum(data1, k)
print("Checksum from  the connected user (client): " + Checksum)

msg = input("Enter receiver message to send: ")
conn.send(msg.encode())

conn.close()



 



