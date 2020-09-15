def accum(s):
    matrix = []
    for i in s:
        matrix.append(i)
    # print(matrix)
    for i in matrix:
        x = i+1*(matrix[i])
    print(x)



accum("abcd")