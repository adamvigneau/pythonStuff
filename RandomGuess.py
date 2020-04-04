import random

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Answer = random.choice(number)
userInput = input("Guess an integer between 1 and 20:\n")


def is_int(test):
    try:
        num = int(test)
    except ValueError:
        return False
    return True


Guess = False
i = 0
while Guess == False and i < 10:
    if is_int(userInput):
        if int(userInput) == Answer:
            print("Correct, you Win!!!")
            Guess = True
        else:
            i += 1
            if int(userInput) < 1 or int(userInput) > 20:
                print("You're not following directions. Try again.")
                userInput = input("Guess an integer between 1 and 20:\n")
            elif int(userInput) < Answer:
                print("Higher than " + userInput)
                userInput = input("Guess an integer between 1 and 20:\n")
            elif int(userInput) > Answer:
                print("Lower than " + userInput)
                userInput = input("Guess an integer between 1 and 20:\n")
    else:
        i += 1
        print("You should look up what an integer is, then try again.")
        userInput = input("Guess an integer between 1 and 20:\n")
if Guess == False and i == 10:
    print("You lost, the number was: " + str(Answer))
