def maxDistance(self, s: str, k: int) -> int:
    x = [0, 0]
    y = [0, 0]
    a = 0
    for i in range(len(s)):
        if (s[i] == "E"):
            x[1] += 1
        elif (s[i] == "W"):
            x[0] += 1
        elif (s[i] == "N"):
            y[1] += 1
        elif (s[i] == "S"):
            y[0] += 1
        z = max(x) + max(y) + k - max(0, min(x) + min(y) - k)
        if (z > a):
            a = z
    return min(a, len(s))

s = "NWSE"
k = 1
print(maxDistance(0,s,k))