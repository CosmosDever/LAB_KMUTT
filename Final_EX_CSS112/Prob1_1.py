def Problem1_1(a):
    return [True if x > 1 and all(x % y != 0 for y in range(2, x)) else False for x in a ]