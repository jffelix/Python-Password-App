from cryptography.fernet import Fernet
from pathlib import Path
# import os

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
    try:
        loadedKey = open(currentPath, "rb").read()
        print(loadedKey)
        return loadedKey
    except:
        print("Error received while loading key")

# print(loadKey())

def passwordEncrypt():
    inputPassword = input("Input your message here: ")

    # load pass key from saved file here
    try:
        loadedPassKey = loadKey()
        print("sucessful key load")
        print("Here is the loaded pass key: ", loadedPassKey)
        return loadedPassKey
    # need to generate new key if not found
    except:
        print("Error received while loading key at passwordEncrypt")
        newKey = generateKey()
        print("Generating new key: ", newKey)

        fernet = Fernet(newKey)

        # convert string to bytes
        encryptMessage = fernet.encrypt(bytes(inputPassword, encoding="utf8"))
    
        print("We have generated a new encrypted password: ")
        return encryptMessage

print(passwordEncrypt())