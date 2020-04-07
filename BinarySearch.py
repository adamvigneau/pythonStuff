import statistics
import pandas

number = [0, 2, 4, 6, 8, 10, 12, 14, 16]  # Could generate this dynamically
userInput = input("Guess an integer between 0 and 100:\n")
checkArr = []


def is_middle(arr, number):
    if number == statistics.median(arr):
        return True
    elif number.between(min(arr), statistics.median(arr)):
        arr = [x for x in arr if x <= statistics.median(arr)]
        return arr
    elif number.between(statistics.median(arr), max(arr)):
        arr = [x for x in arr if x > statistics.median(arr)]
        return arr
    else:
        return False
