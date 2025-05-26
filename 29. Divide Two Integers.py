def divide(self, dividend: int, divisor: int) -> int:
    a = abs(dividend)
    b = abs(divisor)
    x = 0
    y = b
    z = 1
    while (a >= b):
        if (y + y <= a):
            y += y
            z += z
            a -= y
            x += z
        else:
            y = b
            z = 1
            a -= y
            x += z
    if (dividend == 0):
        return 0
    elif ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)):
        if (x > 2 ** 31 - 1):
            return 2 ** 31 - 1
        else:
            return x
    else:
        if (x < -2 ** 31 - 1):
            return -2 ** 31 - 1
        else:
            return -x