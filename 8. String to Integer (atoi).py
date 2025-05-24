def myAtoi(self, s: str) -> int:
    s = s.strip()
    x = ""
    for i in range(len(s)):
        try:
            y = int(s[i])
            x += s[i]
        except:
            if (i == 0 and (s[i] == '+' or s[i] == '-')):
                x += s[i]
            else:
                break
    try:
        return max(-2 ** 31, min(int(x), 2 ** 31 - 1))
    except:
        return 0

s="+-12"
print(myAtoi(0,s))