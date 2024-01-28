from cryptography.fernet import Fernet

inputMessage = input("Input your message here: ")

key = Fernet.generate_key()
fernet = Fernet(key)

encryptMessage = fernet.encrypt(bytes(inputMessage, encoding="utf8"))

print(encryptMessage)