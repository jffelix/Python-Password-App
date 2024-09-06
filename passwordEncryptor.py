from cryptography.fernet import Fernet
# from pathlib import Path

# currentPath = Path(__file__).absolute()
# print(currentPath)

def generateKey():
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # pass key is not saving to file

    # with open("password.key", "wb") as file:
    #     file.write(fernet)
    return fernet

# def loadKey():
#     return open("password.key", "rb").read()
#     # return open(currentPath).read()
#     # print("loadKey test")

# print(loadKey())

def passwordEncrypt():
    inputPassword = input("Input your message here: ")

    # goal is to load pass key from saved file here
    loadKey = generateKey()

    # convert string to bytes
    encryptMessage = loadKey.encrypt(bytes(inputPassword, encoding="utf8"))
    
    print("Here is your encrypted password: ")
    return encryptMessage

print(passwordEncrypt())