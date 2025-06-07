def clearStars(self, s: str) -> str:
    x = s.count("*")
    s = list(s)
    y = dict()

    for i in range(26):
        y[chr(97 + i)] = []
    c_list = list(y.keys())
    for i in range(len(s)):
        if (s[i] != "*"):
            y[s[i]].append(i)
        else:
            x -= 1
            s[i] = ""
            for i in range(26):
                if (len(y[c_list[i]]) == 0):
                    continue
                else:
                    z = y[c_list[i]][-1]
                    y[c_list[i]].pop()
                    s[z] = ""
                    break
        if (x == 0):
            break

    return "".join(s)

s = "aaba*a"
print(clearStars(0,s))