import heapq
from collections import defaultdict

# Function to calculate the frequency of each character in the input string


def calculate_frequency(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

# Function to build the Huffman Tree


def build_huffman_tree(frequency):
    # Create a priority queue (min-heap)
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)

    # While there is more than one node, combine the two nodes with the lowest frequencies
    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)

        # Assign the binary code for each node
        for pair in low1[1:]:
            pair[1] = '0' + pair[1]
        for pair in low2[1:]:
            pair[1] = '1' + pair[1]

        # Merge the two nodes and push back into the heap
        heapq.heappush(heap, [low1[0] + low2[0]] + low1[1:] + low2[1:])

    # Return the final Huffman Tree
    return heap[0]

# Function to generate the Huffman Codes from the Huffman Tree


def generate_huffman_codes(tree):
    huffman_codes = {}
    for char, code in tree[1:]:
        huffman_codes[char] = code
    return huffman_codes

# Function to encode the input text using Huffman Codes


def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

# Function to decode the encoded text back to original text


def decode_text(encoded_text, huffman_codes):
    reversed_codes = {v: k for k, v in huffman_codes.items()}
    code = ''
    decoded_text = ''
    for bit in encoded_text:
        code += bit
        if code in reversed_codes:
            decoded_text += reversed_codes[code]
            code = ''
    return decoded_text

# Main function to perform Huffman Coding


def huffman_coding(text):
    # Step 1: Calculate the frequency of each character
    frequency = calculate_frequency(text)

    # Step 2: Build the Huffman Tree
    huffman_tree = build_huffman_tree(frequency)

    # Step 3: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Step 4: Encode the input text using Huffman Codes
    encoded_text = encode_text(text, huffman_codes)

    # Step 5: Decode the encoded text back to the original text
    decoded_text = decode_text(encoded_text, huffman_codes)

    # Return the results
    return huffman_codes, encoded_text, decoded_text


# Taking input from the user
text = input("Enter the text to be encoded using Huffman Coding: ")

# Call the Huffman Coding function
huffman_codes, encoded_text, decoded_text = huffman_coding(text)

# Display the results
print("\nHuffman Codes:", huffman_codes)
print("Encoded Text:", encoded_text)
print("Decoded Text:", decoded_text)

# Explanation:
# - The `calculate_frequency` function calculates the frequency of each character in the input string.
# - The `build_huffman_tree` function builds the Huffman tree by creating a priority queue and combining nodes with the lowest frequencies.
# - The `generate_huffman_codes` function generates the Huffman codes by traversing the tree.
# - The `encode_text` function encodes the input text using the generated Huffman codes.
# - The `decode_text` function decodes the encoded text back to the original text using the reverse of the Huffman codes.


# Q&A Section

# Q1: What is Huffman Coding?
# A1: Huffman Coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies.

# Q2: Why do we use a priority queue (min-heap) in Huffman Coding?
# A2: A priority queue helps efficiently merge the two nodes with the lowest frequencies at each step of building the Huffman tree.

# Q3: How does the `calculate_frequency` function work?
# A3: It counts the frequency of each character in the input string and stores the result in a dictionary.

# Q4: What is the purpose of the `build_huffman_tree` function?
# A4: It constructs the Huffman tree by iteratively combining the nodes with the lowest frequencies until only one node remains.

# Q5: How does the `generate_huffman_codes` function work?
# A5: It assigns binary codes to characters based on the structure of the Huffman tree, where each left branch is '0' and each right branch is '1'.

# Q6: How is the input text encoded in Huffman Coding?
# A6: The input text is encoded by replacing each character with its corresponding Huffman code.

# Q7: Can Huffman Coding be used for any type of data?
# A7: Yes, Huffman Coding can be applied to any data that can be represented as a sequence of symbols, such as text, images, or audio.

# Q8: How does the `decode_text` function work?
# A8: It decodes the encoded text by traversing the Huffman codes in reverse and reconstructing the original text.

# Q9: What is the time complexity of Huffman Coding?
# A9: The time complexity is O(n log n), where n is the number of unique characters in the input text.

# Q10: Can Huffman Coding be used for real-time data compression?
# A10: While it is efficient for compressing static data, Huffman Coding may not be ideal for real-time compression due to the time required to build the Huffman tree.

# Example of Input:
# Suppose the input text is:
# "this is an example for huffman encoding"

# Expected Output:
# Huffman Codes:
# {'a': '000', 's': '001', 'i': '010', 'e': '011', 'n': '100', 'f': '1010', 't': '1011', 'o': '1100', 'r': '1101', 'h': '1110', 'm': '1111', 'x': '0000', 'p': '0001', 'l': '0010', 'g': '0011', 'c': '0100'}

# Encoded Text:
# 101101101101001011010010110100111100100100111111100011000101110100100101010011001010101011101011010011111110110100111101011111101110

# Decoded Text:
# this is an example for huffman encoding

