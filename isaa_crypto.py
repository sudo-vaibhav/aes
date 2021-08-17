#!/usr/bin/python3
import sys
import aes


def main():
    key_length = 256
    if len(sys.argv)<2:
        input_file = "file_to_encrypt.txt"
        output_file = "encrypted_file.txt"
        key = aes.random_key_generator(int(key_length))
        AES = aes.AES(key, key_length)
        bcm = aes.CBC(AES, 16)
        bcm.cipher(input_file, output_file)
        print("Encryption Successful!!")
        print("Cipher Key:", key)
        write_key(key)

    else:
        key = read_key()
        if key == 1:
            print("File key.txt doesn't exists! Can't decrypt without key")
            exit(1)
        input_file = "encrypted_file.txt"
        output_file = "decrypted_file.txt"
        key_length = len(key) * 4
        AES = aes.AES(key, key_length)
        bcm = aes.CBC(AES, 16)
        bcm.decipher(input_file, output_file)
        print("Decrypted Successfully!!")

def read_key():
    try:
        f = open("key.txt", "r")
    except IOError:
        return 1
    
    key = f.read()
    f.close()
    return key

def write_key(key):
    with open("key.txt", "w") as f:
        f.write(key)
        f.close()

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
