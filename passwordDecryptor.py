from cryptography.fernet import Fernet
from passwordEncryptor import loadKey

def passwordDecrypt():
    try:
        encryptedPassword = input("Type in your encrypted password: ")

        loadingSavedKey = loadKey()
        fernet = Fernet(loadingSavedKey)
        decryptedPassword = fernet.decrypt(encryptedPassword).decode()

        print("Your decrypted password: ", decryptedPassword)
        return decryptedPassword
    
    except:
        print("Error received while decrypting password")