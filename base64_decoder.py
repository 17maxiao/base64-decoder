"""
clue to use base64 is because of the trailing = sign

how to do base64 encoding:
1. split binary code representation of ASCII string into groups of 6 bits
2. convert each group of 6 bits into ASCII using base 10
3. add the = sign however many times is required add a pair of 00s to make the length of final encoded
string be a multiple of 4

how to decode base64:
1. convert ASCII to 6-bit binary
2. remove the 00 pairs denoted by # of == in the original message string
2. convert the binary back into ASCII (8-bit)

Why is base64 used?
Messages will only contain 64 printable ASCII characters instead of the usual full 8 bit range.
That way, during data transmission, we don't have to worry about the initial encoding or how chars
will appears on screen of message recipient

"""

import sys
# import base64

# base64 conversion chart
base64_mapping = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    'a': 26,
    'b': 27,
    'c': 28,
    'd': 29,
    'e': 30,
    'f': 31,
    'g': 32,
    'h': 33,
    'i': 34,
    'j': 35,
    'k': 36,
    'l': 37,
    'm': 38,
    'n': 39,
    'o': 40,
    'p': 41,
    'q': 42,
    'r': 43,
    's': 44,
    't': 45,
    'u': 46,
    'v': 47,
    'w': 48,
    'x': 49,
    'y': 50,
    'z': 51,
    '0': 52,
    '1': 53,
    '2': 54,
    '3': 55,
    '4': 56,
    '5': 57,
    '6': 58,
    '7': 59,
    '8': 60,
    '9': 61,
    '+': 62,
    '/': 63,
}

"""
takes in a base64 encoded string and returns its 6bit binary representation
"""


def base64_to_binary(msg: str):
    # remove the = padding
    msg = msg.replace('=', '')
    binary_msg = []
    for letter in msg:
        # account for base64 indexing (-65 offset)
        char_val = base64_mapping[letter]

        # print(f'test -- {letter} is int: {char_val}')
        binary = [0]*6
        count = 0
        while char_val >= 1:
            quotient = int(char_val % 2)
            binary[5-count] = quotient
            char_val = int(char_val / 2)
            count += 1

        # print(f'test -- {letter} is binary: {binary}')
        binary_msg += binary
    return binary_msg


"""
takes in list of ints representing 8-bit binary representations of ascii characters and returns ascii string
"""


def binary_to_ascii(binary: list[int]):
    # now parse the binaryMsg by 8 bits and convert back to ASCII
    ascii_sum = 0
    decoded_ans = ""
    for i in range(len(binary)):
        count = i % 8  # see which bit we are on out of the 8
        if count == 0:
            # covert to ascii
            decoded_ans += chr(ascii_sum)
            # reset every 8 bits
            ascii_sum = 0

        ascii_sum += int(binary[i])*pow(2, 7-count)

    return decoded_ans[1:]  # cut off first throwaway char


"""
takes in a base64 encoded string and returns its decoded ascii representation
"""


def decode(msg: str):
    # num zeros added for padding
    padding = 2*(msg.count('=') - len(msg))
    # now convert the ASCII into binary
    binary_msg = base64_to_binary(msg)
    # remove zeros added for padding during encoding
    binary_msg = binary_msg[:len(binary_msg)-padding]
    # now parse the binaryMsg by 8 bits and convert back to ASCII
    return binary_to_ascii(binary_msg)


"""
driver code
"""

if __name__ == "__main__":
    msg = "Enter your encoded message here"
    sys.stdout.write(
        f"Message is: {decode(msg)}\n"
    )

    # Check answers against built in python library for base64 encoding for testing
    # sys.stdout.write(
    #     f"Message is: {base64.b64decode(msg)}\n"
    # )
