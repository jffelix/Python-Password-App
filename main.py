print("Welcome to Password Generator!")

userChoice = input("Choose from the following: Generator, Encryptor, Decryptor ")

if (userChoice.lower() == "generator"):
    print("You chose Generator!")
elif (userChoice.lower() == "encryptor"):
    print("You chose Encryptor!")
elif (userChoice.lower() == "decryptor"):
    print('You chose Decryptor!')
else:
    print("Error, choose again.")