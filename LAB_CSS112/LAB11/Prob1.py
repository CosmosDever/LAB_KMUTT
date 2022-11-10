def gen5odds():
    for i in range(1,99,10):
        odd=[j for j in range(i,i+10) if j%2==1]
        yield odd   
def Problem1():
    ans=[]
    for i in gen5odds():
        ans.append(sum(i))
    return ans