from passwordGenerator import passwordGenerate
from passwordEncryptor import passwordEncrypt
from passwordDecryptor import passwordDecrypt

print("Welcome to Python Password App!\n")

userChoice = input("Choose from the following: Generator, Encryptor, Decryptor ")

if (userChoice.lower() == "generator"):
    print("Welcome to Password Generator!\n")
    passwordGenerate()
elif (userChoice.lower() == "encryptor"):
    print("Welcome to Password Encryptor!\n")
    passwordEncrypt()
elif (userChoice.lower() == "decryptor"):
    print("Welcome to Password Decryptor!\n")
    passwordDecrypt()
else:
    print("Your input does not match the choices. Choose again.")