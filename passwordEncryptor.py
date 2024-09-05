from cryptography.fernet import Fernet

# inputMessage = input("Input your message here: ")

# key = Fernet.generate_key()
# fernet = Fernet(key)

# encryptMessage = fernet.encrypt(bytes(inputMessage, encoding="utf8"))

# print("Here is your encrypted password")
# print(encryptMessage)

def passwordEncrypt(inputPassword):
    inputPassword = input("Input your message here: ")
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encryptMessage = fernet.encrypt(bytes(inputPassword, encoding="utf8"))

    print("Here is your encrypted password")
    return encryptMessage

print(passwordEncrypt("password"))