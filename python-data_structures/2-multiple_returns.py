def multiple_returns(sentence):
    L = len(sentence)
    if L == 0:
        first = None
    else:
        first = sentence[0]
    return (L, first)