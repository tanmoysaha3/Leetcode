import math
from collections import Counter

def countBalancedPermutations(self, num: str) -> int:
    if (sum(int(c) for c in num) % 2 != 0):
        return 0
    m, n = 0, 0
    for i in num:
        if (int(i) % 2 == 0):
            m += 1
        else:
            n += 1
    if (len(set(num)) == len(num)):
        e = math.factorial(m) * math.factorial(n)
        h = (m // 2) * (n // 2) * 2
        e = e * max(h, 1)
        return e

    print(-1)
    m = []
    n = []
    for i in num:
        if (int(i) % 2 == 0):
            m.append(i)
        else:
            n.append(i)
    a = dict(Counter(num))
    c = []
    d = []
    for i in a:
        if (int(i) % 2 == 0):
            c.append(i)
        else:
            d.append(i)
    print(c, d)
    e = math.factorial(len(c)) * math.factorial(len(d))
    # e=factorial(len(m))*factorial(len(n))
    # e=e*max((len(c)//2),(len(d)//2),1)
    h = (len(c) // 2) * (len(d) // 2) * 2
    print(e)
    # e=e*max(h,1)
    return e
