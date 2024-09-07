from cryptography.fernet import Fernet
from pathlib import Path

currentPath = Path(__file__).parent / "keyfile.key"

# generates and saves pass key to file
def generateKey():
    key = Fernet.generate_key()

    try:
        with open(currentPath, "wb") as file:
            file.write(key)
        return key
    except:
        print("Error received while generating key.")

# loads saved pass key
def loadKey():
    try:
        loadedKey = open(currentPath, "rb").read()
        return loadedKey
    except:
        print("Error received while loading key at loadKey.")

# accepts input for encryption
def passwordEncrypt():
    inputPassword = input("Input your message here: ")

    newKey = generateKey()
    print("Generated new key and saved to file")

    fernet = Fernet(newKey)

    # convert string to bytes
    encryptMessage = fernet.encrypt(bytes(inputPassword, encoding="utf8"))

    print("Please save this encrypted password for reference: ", encryptMessage)
    return encryptMessage