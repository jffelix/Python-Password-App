from cryptography.fernet import Fernet

def passwordEncrypt():
    inputPassword = input("Input your message here: ")
    key = Fernet.generate_key()
    fernet = Fernet(key)
    # convert string to bytes
    encryptMessage = fernet.encrypt(bytes(inputPassword, encoding="utf8"))

    print("Here is your encrypted password: ")
    return encryptMessage

# print(passwordEncrypt())