#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num=str(number)
last_digit = str(number % 10)
if int(last_digit) > 5:
    result="and is greater than 5"
elif int(last_digit) == 0:
    result="and is 0"
elif (int(last_digit) < 6) and (int(last_digit) != 0):
    result="and is less than 6 and not 0"
print("Last digit of" ,str_num, "is", last_digit,result)