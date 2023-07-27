def update_dictionary(a_dictionary, key, value):
    # Check if the key already exists in the dictionary
    if key in a_dictionary:
        # If yes, replace the existing value with the new value
        a_dictionary[key] = value
    else:
        # If no, add a new key/value pair to the dictionary
        a_dictionary[key] = value
    
    return a_dictionary