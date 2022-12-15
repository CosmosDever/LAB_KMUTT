import Prob3_1
# Question3.2
def Problem3_2():
    agen = Prob3_1.Problem3_1(35)
    for i in range(7):
        try:
            twinprime = next(agen)
        except StopIteration:
            break
        except:
            break
        else:
            print(twinprime)
    return 'Ok'