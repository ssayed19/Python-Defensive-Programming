#! c:\pyhton32/python.exe
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
import base64
import sys

BLOCK_SIZE=16

def encrypt(message, passphrase):
    # passphrase MUST be 16, 24 or 32 bytes long, how can I do that ?
    if len(passphrase) != int(24):
        sys.exit("Byte size is " + str(len(passphrase)) + " bytes! Passphrase MUST be 24 bytes long")
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return base64.b64encode(aes.encrypt(message.encode('utf-8')))

def decrypt(encrypted, passphrase):
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(encrypted.decode('utf-8')))
	
def main():
    message = input("Enter your secret message: ")
    passphrase = Random.new().read(24)
    encrypted = encrypt(message, passphrase)
    print("Encrypted message is: " + str(encrypted))
    decrypted = decrypt(encrypted, passphrase)
    print("Decrypted message is:" + str(decrypted))
main()