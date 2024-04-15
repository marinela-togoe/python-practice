import codecs;
import base64;


def rot_encode(input_string):
     for i in range(1, 27):
        encoded = ''.join(chr((ord(char) - 97 + i) % 26 + 97) if 'a' <= char <= 'z' else 
                          chr((ord(char) - 65 + i) % 26 + 65) if 'A' <= char <= 'Z' else char
                          for char in input_string)
        print(f'ROT{i}: {encoded}')

def base64_encode_decode(input_string):
    encoded = base64.b64encode(input_string.encode())       
    decoded = base64.b64decode(encoded).decode()
    print(f'\nBase64 Encoded: {encoded.decode()}')
    print(f'Base64 Decoded: {decoded}')

if __name__ == "__main__":
    input_string = input("Enter a string to encode/decode: ")
    rot_encode(input_string)
    base64_encode_decode(input_string)
