def is_same_class(obj, a_class):
    result = isinstance(obj, a_class)
    if result:
        return True
    else:
        return False