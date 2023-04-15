def crc(message, key):
    # Pad the message with zeros at the end to accommodate for the key
    message += '0' * (len(key) - 1)
    # Convert the message and key to lists of bits
    message = list(message)
    key = list(key)
    # Loop through each bit in the message
    for i in range(len(message) - len(key) + 1):
        # If the current bit is 1, XOR the key with the message
        if message[i] == '1':
            for j in range(len(key)):
                message[i + j] = str(int(message[i + j]) ^ int(key[j]))
    # Return the remainder (the last len(key) - 1 bits of the message)
    return ''.join(message[-(len(key)-1):])

# Prompt the user to enter the message and key
message = input("Enter the message: ")
key = input("Enter the key: ")

# Calculate the CRC and append it to the message
crc_code = crc(message, key)
msg = message + crc_code

print(f"The CRC is: {crc_code}")

# Print the message with the CRC
print(f"The message with CRC is: {msg}")
