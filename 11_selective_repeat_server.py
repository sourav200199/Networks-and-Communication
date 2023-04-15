# Server side of selective repeat protocol
# Take three two cases - ack received and ack timeout (ack not sent)

import socket
import time

# Create a TCP/IP socket
server = socket.socket()
server.bind(('localhost', 12345))
server.listen(5)

# Accept the connection
conn, addr = server.accept()

# Receive the data, send the ack
while True:
    data = conn.recv(1024).decode()
    
    if data == 'exit':
        break
    
    print('Received: ', data)
    # case 2: ack not sent
    if data == 'test':
        print('Not sending the ack')
        # Wait for the same packet again
        data = conn.recv(1024).decode()
        print('Received: ', data)
        # Send the ack
        conn.send('test'.encode())
        print('Sent: ack')
    else:
        conn.send(str(data).encode())
        print('Sent Acknowledgement: ', data)

conn.close()