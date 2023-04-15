# Client side of the Go-back-n protocol
# Test cases -
# 1.Window successfully slides
# 2. Acknowledgement lost
import time
import socket

# Create a UDP socket
client = socket.socket()
client.connect(('localhost', 12345))

# Send data
frame = input("Enter the frame to be sent: ")
window = int(input("Enter the window size: "))

count_ack = 0

# Send the data - window by window
for i in range(0, len(frame), window):
    #client.send(frame[i:i+window].encode())
    #Send each char. of the window with a delay of 1 second
    for j in frame[i:i+window]:
        client.send(j.encode())
        time.sleep(1)
        print(f'Sent: {j}')

    client.settimeout(3)
    try:
        ack = client.recv(1024).decode()
        print('Received: ', ack)
        count_ack += 1
    #Check if ack is received for all the char. of the frame, then only slide the window
    except socket.timeout:
        if count_ack == len(frame[i:i+window]):
            print("Acknowledgement received for all the characters")
            print("Sliding the window")
        else:
            print("Acknowledgement not received for all the characters")
            print("Resending the frame")
            break
        count_ack = 0

client.close()