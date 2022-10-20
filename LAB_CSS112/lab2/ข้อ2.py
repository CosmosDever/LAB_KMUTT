Num=int(input('Enter number '))
def Summationt(n):
    if n==0:
        return 0
    else: return n+Summationt(n-1)
print(f'Summation of numbers from 1 to {"%.0f" % Num} is: {"%.0f" % Summationt(Num)}')