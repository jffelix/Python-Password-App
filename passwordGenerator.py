import random
import string

def passwordGenerate():

    plength = int(input("Enter password length: "))

    lowercaseLetters = string.ascii_lowercase
    uppercaseLetters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    keyboardCommands = []

    keyboardCommands.extend(list(lowercaseLetters))
    keyboardCommands.extend(list(uppercaseLetters))
    keyboardCommands.extend(list(numbers))
    keyboardCommands.extend(list(symbols))

    generatedPassword = ''

    while True:
        randomInput = random.choice(keyboardCommands)
        generatedPassword += randomInput
        plength -= 1
        if plength == 0:
            break

    print("Your new password is: " + generatedPassword)
    return generatedPassword

# print(passwordGenerate())