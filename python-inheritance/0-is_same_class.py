def is_same_class(obj, a_class):
    """
    This function checks if a class is instance or what
    """
    result = isinstance(obj, a_class)
    if result:
        return True
    else:
        return False