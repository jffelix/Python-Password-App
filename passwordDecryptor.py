from cryptography.fernet import Fernet
from passwordEncryptor import passwordEncrypt, loadKey

encryptedPassword = passwordEncrypt()

def passwordDecrypt():

    # will need to load saved pass key from passwordEncryptor file here
    try:
        loadingSavedKey = loadKey()
        print("Successfully loaded encryptedPassword at passwordDecryptor: ", encryptedPassword)
        print("succesfully loaded key at passwordDecryptor: ", loadingSavedKey)
        fernet = Fernet(loadingSavedKey)

        decryptedPassword = fernet.decrypt(encryptedPassword).decode()
        return decryptedPassword
    except:
        print("Error received while loading key at passwordDecryptor")

print(passwordDecrypt())