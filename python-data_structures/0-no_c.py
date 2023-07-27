def no_c(my_string):
    L = len(my_string)
    new_str = my_string
    for i in range (L):
        if my_string[i] == "c" or my_string[i] == "C":
            new_str = my_string[:i] + my_string[i + 1:]
            
    return new_str