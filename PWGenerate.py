import random
import string
from _ast import Break

userInput = input("How long would you like your password to be? Minimum length of six characters\n")
password = ''
passwordChoice = string.printable  # all ascii characters
i = 0

def is_int(test):
    try:
        num = int(test)
    except ValueError:
        return False
    return True


while True:
    if is_int(userInput) and int(userInput) >= 6:  # setting min password length
        while i < int(userInput):
            password += passwordChoice[random.randint(0, len(passwordChoice)-1)]
            i += 1
        print(password)
        break
    elif is_int(userInput) and int(userInput) < 6:
        userInput = input("Minimum length of six characters required. Try again.")
    else:
        userInput = input("Sorry, could you repeat that?")
