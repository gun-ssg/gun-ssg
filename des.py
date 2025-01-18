from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def des_encrypt_ecb(text, key):


    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters (8 bytes).")

    key = key.encode('utf-8')
    text = text.encode('utf-8')
    text = "{:0>16x}".format(int.from_bytes(text, 'big'))
    text = bytearray.fromhex(text)

    text_padded = pad(text, DES.block_size)

   
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(text_padded)

    return encrypted_bytes.hex().upper()

text = input("Enter a string to encrypt (max 8 characters): ")
key = input("Enter an 8-character encryption key: ")

encrypted_text = des_encrypt_ecb(text, key)
print("Encrypted Hex:", encrypted_text)
