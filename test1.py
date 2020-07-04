"""import time
seconds = int(input ("how many seconds to wait?"))
for i in range(seconds):
    print (str(seconds - i) + " second remain")
    time.sleep(1)

print("TIME IS UP!")
"""


def count_numbers(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print("Cannot add letters")
    except ValueError:
        print("Only numbers are allowed")
    except Exception:
        print("Something went wrong!")
"""
number = input("give a number")
number2 = input("give a number")
print(count_numbers(number, number2))
"""
print(count_numbers(2, 2))