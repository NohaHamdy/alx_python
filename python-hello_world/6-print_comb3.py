for i in range(9):
    for j in range(i+1,10):
        if (i == 8) and (j == 9):
            print("{}{}".format(i,j),end="\n")
            break
        else:
            print("{}{},".format(i,j),end=" ")