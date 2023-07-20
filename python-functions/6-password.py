def validate_password(password):
    space = 1
    length = 0
    upper = 0
    lower = 0
    digit = 0
    if (len(password) >= 8):
        length = 1
        for i in range(len(password)):
            if (password[i].isupper()):
                upper = 1
            if (password[i].islower()):
                lower = 1
            if (password[i].isdigit()):
                digit = 1
            if (password[i].isspace()):
                space = 0
    if (length == 1) and (upper == 1) and (lower == 1) and (space == 1) and (digit == 1):
        return (True)
    else:
        return (False)
    
    
print(validate_password("password123"))