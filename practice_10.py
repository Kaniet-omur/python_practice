import random

matrix_1 = []

for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(0, 10))
    matrix_1.append(row)
print(matrix_1)


matrix_2 = []

for i in range(10):
    row=[]
    for j in range(10):
        row.append(random.randint(0, 10))
        matrix_2.append(row)
print(matrix_2)


matrix_3 = [[0] * 10 for i in range(10)]

for i in range(len(matrix_1)):
    for i in range(len(matrix_1[0])):
        matrix_3[i][j] = matrix_1 + matrix_2[i][j]

print(matrix_3)