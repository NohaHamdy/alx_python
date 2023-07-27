def print_matrix_integer(matrix=[[]]):
    L = len(matrix)
    for i in range (L):
        for j in range (len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end = " ")
        print()