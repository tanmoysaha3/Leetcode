#Brute Force
from collections import deque

def lengthAfterTransformations(self, s: str, t: int) -> int:
    MOD = 10 ** 9 + 7
    queue = deque()
    a = []
    c = dict()
    for i in range(len(s)):
        b = 123 - ord(s[i])
        if (b not in c):
            c[b] = 1
            a.append(b)
        else:
            c[b] += 1
    a.sort()

    for i in a:
        queue.append(i)
    x = len(s)
    while (True):
        first = queue.popleft()
        y = c[first]
        del c[first]

        if (first > t):
            break

        if (first + 25 not in c):
            c[first + 25] = y
            queue.append(first + 25)
        else:
            c[first + 25] += y

        if (first + 26 not in c):
            c[first + 26] = y
            queue.append(first + 26)
        else:
            c[first + 26] += y
        x += y
        x = x % MOD
    return x

print(lengthAfterTransformations(0,"jqktcurgdvlibczdsvnsg",7517))