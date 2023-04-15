# Client side of the selective repeat protocol
# Take three two cases - ack received and ack timeout (ack not sent)

import socket
import time

# Create a TCP/IP socket
client = socket.socket()
client.connect(('localhost', 12345))

# Send the data, wait for the ack
data = input('Enter data: ')
window = int(input('Enter the window size: '))

# Send the data window by window, wait for the ack
for i in range(0, len(data), window):
    # Send the data
    client.send(data[i:i+window].encode())
    print(f'Sent: {data[i:i+window]}')
    # Wait for the ack
    client.settimeout(3)
    try:
        ack = client.recv(1024).decode()
        print('Received: ', ack)
    except socket.timeout:
        print('Timeout. Resending the packet')
        # Resend the packet
        client.send(data[i:i+window].encode())
        print(f'Sent: {data[i:i+window]} again')
        # Wait for the ack
        ack = client.recv(1024).decode()
        print('Received: ', ack)
