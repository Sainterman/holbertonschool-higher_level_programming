#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and (abs(number) % 10) != 0:
    print("Last digit of {:d} is -{:d}"
          .format(number, abs(number) % 10), end=' ')
else:
    print("Last digit of {:d} is {:d}"
          .format(number, abs(number) % 10), end=' ')
if (abs(number) % 10) > 5:
    print("and is greater than 5")
elif (abs(number) % 10) == 0:
    print("and is 0")
elif (abs(number) % 10) < 6:
    print("and is less than 6 and not 0")
