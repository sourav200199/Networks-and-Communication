# 1. Get input
data = input("Enter the actual data bits: ") 
data = list(data)
data = [int(i) for i in data] # Convert string to int

print("The data bits are: ", data)
num = len(data)
code = []

# --------------------- Functions ---------------------
# Function to check parity
def check_parity(data, start, end):
    parity = 0
    for i in range(start, end, 2**(start+1)): # 2**(start+1) is the step size
        for j in range(i, i+2**start):        # 2**start is the length of the block
            if j < end:                       # To avoid index out of range
                parity = parity + data[j] 
    return parity % 2

# Function to find r bits
def find_r(num):
    r = 0
    while(2**r < num + r + 1):
        r += 1
    return r

# Function to find codeword
def hammingcode(data, num):
    r = find_r(num)
    print("The no. of r bits are: ", r)

    n = num + r
    m = 0
    j = 0

    for i in range(1, n+1):
        if i == 2**m and m <= r:
            code.insert(i-1, 0)
            m += 1
        else:
            code.insert(i-1, data[j])
            j += 1

    m = 0
    for i in range(1, n+1):
        if i == 2**m and m <= r:
            code[i-1] = check_parity(code, i-1, n)
            m += 1

    print("The codeword is: ", code)

# Function to find Syndrome bits
def finderror(received, r, m):
    j = 0
    c = 0

    for i in range(1, len(received)+1):
        if i == 2**m and m <= r:
            c = c + ((2**j) * check_parity(received, i-1, len(received))) # Syndrome bits
            j += 1
            m += 1

    if c == 0:
        print("There is no error in the received codeword.")
    else:
        print("The error is at position: ", (c))
        if received[c-1] == 0:
            received[c-1] = 1
        else:
            received[c-1] = 0
        print("The corrected codeword is: ", received)

# --------------------- Main ---------------------
hammingcode(data, len(data))

# 4. Implement algorithm to find Syndrome bits without error bits
received = input("Enter the received codeword: ")
received = list(received)
received = [int(i) for i in received] # Convert string to int

print("The received codeword is: ", received)

syndrome = []
m = 0

finderror(received, find_r(len(data)), m)




