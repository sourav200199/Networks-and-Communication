#Client side of stop and wait protocol
#Take three test cases - ack received, packet loss and ack timeout
#In the first case, the ack is received and the client sends the next packet
#In the second case, the ack is not received and the client sends the same packet again
#In the third case, the ack is not received within the timeout period and the client sends the same packet again

import socket
import time

# Create a TCP/IP socket
client = socket.socket()
client.connect(('localhost', 12345))

# Send the data, wait for the ack
while True:
    data = input('Enter data: ')
    client.send(data.encode())

    if data == 'exit':
        break
    
    print('Sent: ', data)
    # Wait for the ack
    client.settimeout(3)
    try:
        ack = client.recv(1024).decode()
        print('Received: ', ack)
    except socket.timeout:
        print('Timeout. Resending the packet')
        # Resend the packet
        client.send(data.encode())
        print(f'Sent: {data} again')
        # Wait for the ack
        ack = client.recv(1024).decode()
        print('Received: ', ack)

client.close()

