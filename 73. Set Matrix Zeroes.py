from typing import List


def setZeroes(self, matrix: List[List[int]]) -> None:
    z = len(matrix[0])
    x = False
    y = set()
    for row in matrix:
        for j in range(z):
            if (row[j] == 0):
                x = True
                y.add(j)
        if (x == True):
            row[:] = [0] * z
            x = False

    for row in matrix:
        for i in y:
            row[i] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(0,matrix)
print(matrix)