def Problem1_1(a):
    return True if a > 1 and all(a % y != 0 for y in range(2, a)) else False