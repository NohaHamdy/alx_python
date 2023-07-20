def is_prime(number): 
    if (number == 1):
        return (True)
    elif (number == 0):
        return (False)
    else:
        for i in range (2,10):
            if ((number % i) == 0):
                return (False)
    return (True)
