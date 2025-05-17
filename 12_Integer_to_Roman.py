def intToRoman1(self, num: int) -> str:
    x = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    y = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    i = 0
    z = ""
    while (num != 0):
        if (num // x[i] == 0):
            i += 1
        else:
            z += y[i] * (num // x[i])
            num = num % x[i]
    return z

print(intToRoman1(0,3755))

def intToRoman2(self, num: int) -> str:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    IV = 4
    IX = 9
    XL = 40
    XC = 90
    CD = 400
    CM = 900
    b = ""
    while (num > 0):
        if (num - 1000 >= 0):
            b = b + "M"
            num = num - M
        elif (num - 900 >= 0):
            b = b + "CM"
            num = num - CM
        elif (num - 500 >= 0):
            b = b + "D"
            num = num - D
        elif (num - 400 >= 0):
            b = b + "CD"
            num = num - CD
        elif (num - 100 >= 0):
            b = b + "C"
            num = num - C
        elif (num - 90 >= 0):
            b = b + "XC"
            num = num - XC
        elif (num - 50 >= 0):
            b = b + "L"
            num = num - L
        elif (num - 40 >= 0):
            b = b + "XL"
            num = num - XL
        elif (num - 10 >= 0):
            b = b + "X"
            num = num - X
        elif (num - 9 >= 0):
            b = b + "IX"
            num = num - IX
        elif (num - 5 >= 0):
            b = b + "V"
            num = num - V
        elif (num - 4 >= 0):
            b = b + "IV"
            num = num - IV
        elif (num - 1 >= 0):
            b = b + "I"
            num = num - I
    return b
print(intToRoman2(0,3749))