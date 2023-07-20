def fibonacci_sequence(n):
    FL=[]
    for index in range (n):
        if index < 2:
            value = index;
        else:
            value = FL[index-1] + FL[index-2];
        FL.append(value)
    return (FL)
