from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def des_encrypt_ecb(text, key):
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters (8 bytes).")
    key = key.encode('utf-8')
    text_padded = pad(text, DES.block_size)


    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(text_padded)
    return encrypted_bytes.hex()

def generate(plaintext, difference=None):
    plaintext = plaintext.encode('utf-8')
    plaintext = "{:0>16x}".format(int.from_bytes(plaintext, 'big'))
    plaintext = bytearray.fromhex(plaintext)

    if difference is None:
        return plaintext


    scrambled = bytearray(p ^ d for p, d in zip(plaintext, difference))
    return plaintext, scrambled



text = input("Enter a string to encrypt and scramble (max 8 characters): ")
key = input("Enter an 8-character encryption key: ")


difference = bytearray([0x40, 0x08, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00])


original, scrambled = generate(text, difference)
encrypted_original = des_encrypt_ecb(original, key)
encrypted_scrambled = des_encrypt_ecb(scrambled, key)


print("\nResults:")
print("Original Plaintext (Hex):", original.hex().upper())
print("Scrambled Plaintext (Hex):", scrambled.hex().upper())
print("Encrypted Original Text (Hex):", encrypted_original.upper())
print("Encrypted Scrambled Text (Hex):", encrypted_scrambled.upper())
