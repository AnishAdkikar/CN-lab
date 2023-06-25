def generate_hamming_code(data):
    # Calculate the number of parity bits required
    parity_bits = 0
    while 2**parity_bits < len(data) + parity_bits + 1:
        parity_bits += 1
    
    # Create an array with the required size to hold the data and parity bits
    hamming_code = [None] * (len(data) + parity_bits)
    
    # Copy the data bits to their respective positions in the Hamming code
    j = 0  # index for data bits
    k = 0  # index for Hamming code
    for i in range(len(hamming_code)):
        if i == 2**k - 1:
            hamming_code[i] = None  # Placeholder for parity bit
            k += 1
        else:
            hamming_code[i] = int(data[j])
            j += 1
    
    # Calculate the values of the parity bits
    for i in range(parity_bits):
        parity_index = 2**i - 1
        parity_value = 0
        for j in range(parity_index, len(hamming_code), 2**(i+1)):
            for k in range(j, min(j + 2**i, len(hamming_code))):
                if hamming_code[k] == 1:
                    parity_value ^= 1
        print(hamming_code)
        hamming_code[parity_index] = parity_value
    
    return hamming_code


def detect_error_hamming_code(hamming_code):
    # Calculate the number of parity bits used in the Hamming code
    parity_bits = 0
    while 2**parity_bits < len(hamming_code):
        parity_bits += 1
    
    error_bits = []  # Track the positions of the error bits
    for i in range(parity_bits):
        parity_index = 2**i - 1
        parity_value = 0
        for j in range(len(hamming_code)):
            if j & (2**i - 1) != parity_index and hamming_code[j] == 1:
                parity_value ^= 1
        if parity_value != hamming_code[parity_index]:
            error_bits.append(parity_index + 1)
    
    return error_bits


# Example usage:
data_bits = "1011001"  # Input data bits
hamming_code = generate_hamming_code(data_bits)
print("Hamming code:", hamming_code)

# Simulate an error by flipping a bit in the Hamming code
hamming_code[3] = 1

# Detect and correct the error
error_bit = detect_error_hamming_code(hamming_code)
if error_bit is None:
    print("No error detected.")
else:
    print("Error detected at bit:", error_bit)
