#!/usr/bin/python3
import random
number = random.randint(-10, 10)
msg = "positive" if number > 0 else "zero" if number == 0 else "negative"
print(number, "is", msg)
