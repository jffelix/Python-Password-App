from cryptography.fernet import Fernet
from passwordEncryptor import passwordEncrypt

encryptedPassword = passwordEncrypt()

# def passwordDecryptor():

#     # will need to load saved pass key from passwordEncryptor file here

#     decryptedPassword = fernet.decrypt(encryptedPassword)
#     return decryptedPassword

# print(passwordDecryptor())