# Client side of the Go-back-n protocol
# Test cases -
# 1.Acknowledgement successfully received
# 2. Acknowledgement lost

import socket

# Create a UDP socket
server = socket.socket()
server.bind(('localhost', 12345))
server.listen(5)

conn, addr = server.accept()

count = 0
t = 0
# Receive data
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Received: ", data)

    # Send acknowledgement for each char. of the frame as soon as it is received
    for i in data:
        # case 1: Acknowledgement successfully sent
        conn.send(i.encode())
        print(f'Sent: {i}')
        count += 1
        # case 2: Acknowledgement not sent
        if count == 2 and t < 2:
            print("Acknowledgement not sent")
            t += 1
            break
        

conn.close()
