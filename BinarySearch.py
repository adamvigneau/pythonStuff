import random

testArr = []
for i in range(10):  # Generate 10 random integers
    testArr.append(random.randrange(0, 101))

userInput = int(input("Guess an integer between 0 and 100:\n"))


def binary_search(arr, x, y, num):
    while x <= y:

        med = x + (y - x) // 2

        # Check if x is present at mid
        if arr[med] == num:
            return med

        # If x is greater, ignore left half
        elif arr[med] < num:
            x = med + 1

        # If x is smaller, ignore right half
        else:
            y = med - 1

        # If we reach here, then the element was not present
    return "Integer not present in array"


result = binary_search(testArr, 0, len(testArr) - 1, userInput)
print(result)
