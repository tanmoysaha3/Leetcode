def romanToInt(self, s: str) -> int:
    y = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
         'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}
    x = 0
    s += 'B'
    for i in range(len(s) - 1):
        x += y.get(s[i:i + 2], 0) + y.get(s[i])
    return x
print((romanToInt(0,"MCMXCIV")))