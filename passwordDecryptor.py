from cryptography.fernet import Fernet
from passwordEncryptor import passwordEncrypt, loadKey

# encryptedPassword = passwordEncrypt()

def passwordDecrypt():

    try:
        loadingSavedKey = loadKey()
        encryptedPassword = input("Type in your encrypted password: ")
        fernet = Fernet(loadingSavedKey)
        decryptedPassword = fernet.decrypt(encryptedPassword).decode()
        print("decryptedPassword: ", decryptedPassword)

        return decryptedPassword
    
    except:
        print("Error received while decrypting password")