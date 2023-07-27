def best_score(a_dictionary):
    
    best_score = None
    best_key = None
    
    for key, value in a_dictionary.items():
        if isinstance(value, int) and (best_score is None or value > best_score):
            best_score = value
            best_key = key
    
    return best_key