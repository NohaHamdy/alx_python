#!/usr/bin/env python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        return a/b
        print("Inside result: {}".format(result))
    