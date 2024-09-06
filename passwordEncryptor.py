from cryptography.fernet import Fernet
from pathlib import Path
# import os

# os.listdir()
currentPath = Path(__file__).parent / "keyfile.key"

def generateKey():
    key = Fernet.generate_key()

    try:
        with open(currentPath, "wb") as file:
            file.write(key)
        return key
    except:
        print("Error received while generating key.")

def loadKey():
    try:
        loadedKey = open(currentPath, "rb").read()
        print(loadedKey)
        return loadedKey
    except:
        print("Error received while loading key at loadKey.")

def passwordEncrypt():
    inputPassword = input("Input your message here: ")

    newKey = generateKey()
    print("Generated new key and saved to file")

    fernet = Fernet(newKey)

    # convert string to bytes
    encryptMessage = fernet.encrypt(bytes(inputPassword, encoding="utf8"))

    print("We have generated a new encrypted password: ", encryptMessage)
    return encryptMessage