def differenceOfSums(self, n: int, m: int) -> int:
    return (n * (n + 1) // 2) - ((n // m) * ((n // m) + 1) * m)

n = 10
m = 3
print(differenceOfSums(0,n,m))