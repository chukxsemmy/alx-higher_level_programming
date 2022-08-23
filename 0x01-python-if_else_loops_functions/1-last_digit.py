#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10 if number >= 0 else ((-number % 10) * -1)
msg = f"Last digit of {number} is {lastDigit}"

if lastDigit == 0:
    print(f"{msg} and is 0")

elif lastDigit > 5 and lastDigit % 10 != 0:
    print(f"{msg} and is greater than 5")

else:
    print(f"{msg} and is less than 6 and not 0")
