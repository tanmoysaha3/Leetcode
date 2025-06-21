from collections import Counter


def minimumDeletions(self, word: str, k: int) -> int:
    cout = dict(Counter(word))
    x = list(cout.keys())
    b = []
    for i in range(len(x)):
        y = cout[x[i]]
        z = 0
        for j in range(len(x)):
            if (i == j or y <= cout[x[j]] <= y + k):
                continue
            elif (cout[x[j]] < y):
                z += cout[x[j]]
            elif (cout[x[j]] > y + k):
                z += cout[x[j]] - (y + k)
        b.append(z)
        z = 0
        for j in range(len(x)):
            if (i == j or y - k <= cout[x[j]] <= y):
                continue
            elif (cout[x[j]] < y - k):
                z += cout[x[j]]
            elif (cout[x[j]] > y):
                z += cout[x[j]] - y
        b.append(z)
    return min(b)

word = "dabdcbdcdcd"
k = 2
print(minimumDeletions(0,word, k))