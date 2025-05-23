
import math
def clumsy(self, n: int) -> int:
    y = []
    for i in range(n, 0, -4):
        m = i
        if (i - 1 > 0):
            m = m * (i - 1)
        if (i - 2 > 0):
            m = m / (i - 2)
        y.append(math.floor(m))
    z = y[0]
    j = 1
    if (n - 3 > 0):
        for i in range(n - 3, 0, -4):
            z += i
            if (i - 1 > 0 and len(y) > j):
                z -= y[j]
            j += 1
    return z
print(clumsy(0,10))