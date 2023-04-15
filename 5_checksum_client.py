#Checksum client
import socket

# Create a socket object
host = socket.gethostname()
port = 5000

client_socket = socket.socket()
client_socket.connect((host,port))

message = input("Enter the message -> ")
client_socket.send(message.encode())

# ------------ The Checksum Code ---------------
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

print("Checksum is: ", findChecksum(message, 8))
checksum = findChecksum(message, 8)
client_socket.send(checksum.encode())

data = client_socket.recv(1024).decode()
print('Received from server: ' + data)
received_checksum = findChecksum(data, 8)
print("Receiver Checksum is: ", received_checksum)

if(received_checksum == checksum):
    print("Receiver Checksum == 0. NO ERROR DETECTED!")     
else:
    print("Receiver Checksum != 0. ERROR DETECTED!")

# close the connection
client_socket.close()