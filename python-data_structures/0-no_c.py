def no_c(my_string):
    L = len(my_string)
    new_str = my_string
    for i in range (L):
        if my_string[i] == "c" or my_string[i] == "C":
            if i == 0:
                new_str = my_string[1:]
            else:
                new_str = new_str[:i] + new_str[i + 1:]      
    return new_str