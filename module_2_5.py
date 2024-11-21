def matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

print(matrix(2,2,10))
print(matrix(3,5,42))
print(matrix(4,2,13))