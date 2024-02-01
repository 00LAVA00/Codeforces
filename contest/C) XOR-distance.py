# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    a, b, r = map(int, input().split())
    
    # Calculate the XOR of a and b
    xor_value = a ^ b
    
    # Calculate the minimum value
    if xor_value <= r:
        print(xor_value)
    else:
        print(r)
