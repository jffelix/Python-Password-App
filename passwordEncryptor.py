from cryptography.fernet import Fernet
from pathlib import Path
import os

# os.listdir()
currentPath = Path(__file__).parent / "keyfile.key"
# print(currentPath)

def generateKey():
    key = Fernet.generate_key()

    # pass key is not saving to file. Should use a try/except when handling files
    with open(currentPath, "wb") as file:
        file.write(key)
    return key

def loadKey():
    # return open("password.key", "rb").read()
    return open(currentPath, "rb").read()
    # print("loadKey test")

# print(loadKey())

# def passwordEncrypt():
#     inputPassword = input("Input your message here: ")

#     # goal is to load pass key from saved file here
#     loadKey = generateKey()

#     # convert string to bytes
#     encryptMessage = loadKey.encrypt(bytes(inputPassword, encoding="utf8"))
    
#     print("Here is your encrypted password: ")
#     return encryptMessage

# print(passwordEncrypt())