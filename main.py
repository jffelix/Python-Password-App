from passwordGenerator import passwordGenerate

print("Welcome to Python Password App!")

userChoice = input("Choose from the following: Generator, Encryptor, Decryptor ")

if (userChoice.lower() == "generator"):
    print("Hello from Password Generator!")
    passwordGenerate()
elif (userChoice.lower() == "encryptor"):
    print("You chose Encryptor!")
elif (userChoice.lower() == "decryptor"):
    print('You chose Decryptor!')
else:
    print("Error, choose again.")