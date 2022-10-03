print("NIM : 20210801348")
print("Ketrin Vani Andini")

#operator assigment
a = 10
b = 5

print(a + b)
print(a - b)
print(a / b)
print(a * b)

print("Program penjumlahan matrix ordo 2*2")

matrix1 = [
    [4, 7],
    [4, 9],
]
matrix2 = [
    [5, 10],
    [9, 8],
]

for x in range(0, len(matrix1)):
    for y in range(0, len(matrix1[0])):
        print(matrix1[x][y] + matrix2[x][y], end=' ')
    print(' ')