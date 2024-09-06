from cryptography.fernet import Fernet
from passwordEncryptor import passwordEncrypt, loadKey

encryptedPassword = passwordEncrypt()

def passwordDecryptor():

    # will need to load saved pass key from passwordEncryptor file here
    try:
        loadingSavedKey = loadKey()
        fernet = Fernet(loadingSavedKey)

        decryptedPassword = fernet.decrypt(loadingSavedKey)
        return decryptedPassword
    except:
        print("Error received while loading key at passwordDecryptor")

print(passwordDecryptor())