def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    x = set()
    for i in range(len(s1)):
        z = {s1[i], s2[i]}
        to_remove = []
        for j in x:
            if s1[i] in j or s2[i] in j:
                z.update(j)
                to_remove.append(j)
        for j in to_remove:
            x.remove(j)
        x.add(frozenset(z))

    b = dict()
    for i in x:
        min_i = min(i)
        for j in i:
            b[j] = min_i

    c = ""
    for i in range(len(baseStr)):
        if (baseStr[i] in b):
            c += b[baseStr[i]]
        else:
            c += baseStr[i]

    return c
s1 = "nenneefjelfbkajjmlabiejfkfiidjigdogirrngplqkfpjcnk"
s2 = "podnbcmknqbkfdarngigdorlfofcegbbnbkhhgopcofjegqdqd"
baseStr = "yvqnetdqbqoaejikjgcmmeqcdgvektmppufeoszxquoipoyuxh"
print(smallestEquivalentString(0,s1,s2,baseStr))
