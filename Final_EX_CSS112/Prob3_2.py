import Prob3_1
# Question3.2
def Problem3_2():
    agen = Prob3_1.Problem3_1(35)
    for i in range(7):
        #Your code here try
        twinprime = next(agen)
        #Your code here except
        print(twinprime)
    return 'Ok'