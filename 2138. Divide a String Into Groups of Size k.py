from typing import List


def divideString(self, s: str, k: int, fill: str) -> List[str]:
    n = len(s)
    y = n%k
    if (y != 0):
        s += fill * (k - y)
    x = []
    for i in range(0, n, k):
        x.append(s[i:i + k])
    # print(x)
    return x

s = "abcdefghij"
k = 3
fill = "x"
print(divideString(0,s,k,fill))