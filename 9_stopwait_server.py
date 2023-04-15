# Server side stop and wait protocol
#Take two test cases - ack sent and ack not sent
#In the first case, the ack is sent and the server waits for the next packet
#In the second case, the ack is not sent and the server waits for the same packet again

import socket
import time

# Create a TCP/IP socket
server = socket.socket()
server.bind(('localhost', 12345))
server.listen(5)

# Accept the connection
conn, addr = server.accept()

tt = 0
# Receive the data, send the ack
while True:
    # Test case 1: ack sent
    data = conn.recv(1024).decode()
    
    if data == 'exit':
        break
    
    print('Received: ', data)
    # Send the ack
    # Test case 2: ack not sent
    if data == 'test' and tt==0:
        print('Not sending the ack')
        # Wait for the same packet again
        data = conn.recv(1024).decode()
        print('Received: ', data)
        # Send the ack
        conn.send('test'.encode())
        print('Sent: ack')
        tt = 1

    else:
        conn.send(str(data).encode())
        print('Sent Acknowledgement: ', data)

conn.close()

