def common_elements(set_1, set_2):

    common = set()
    
    for elem in set_1:
        if elem in set_2:
            common.add(elem)
    
    return common