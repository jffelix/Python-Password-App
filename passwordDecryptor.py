from cryptography.fernet import Fernet
from passwordEncryptor import passwordEncrypt

encryptedPassword = passwordEncrypt()

def passwordDecryptor():

    print(encryptedPassword)

print(passwordDecryptor())