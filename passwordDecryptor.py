from cryptography.fernet import Fernet
from passwordEncryptor import passwordEncrypt

encryptedPassword = passwordEncrypt()

# def passwordDecryptor():

#     fernet = Fernet(key)
#     decryptedPassword = fernet.decrypt(encryptedPassword)
#     return decryptedPassword

# print(passwordDecryptor())