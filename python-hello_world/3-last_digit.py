#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num=str(number)
last_digit = str_num[-1]
if int(last_digit) > 5:
    result="and is greater than 5"
elif int(last_digit) == 0:
    result="and is 0"
else:
    result="and is less than 6 and not 0"
print("Last digit of" ,str_num, "is", last_digit,result)