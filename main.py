from passwordGenerator import passwordGenerate
from passwordEncryptor import passwordEncrypt
from passwordDecryptor import passwordDecrypt

print("Welcome to Python Password App! \n")

userChoice = input("Choose from the following: Generator, Encryptor, Decryptor ")

if (userChoice.lower() == "generator"):
    print("Hello from Password Generator!")
    passwordGenerate()
elif (userChoice.lower() == "encryptor"):
    print("Hello from Password Encryptor!")
    passwordEncrypt()
elif (userChoice.lower() == "decryptor"):
    print("Hello from Password Decryptor!")
    passwordDecrypt()
else:
    print("Your input does not match the choices. Choose again.")