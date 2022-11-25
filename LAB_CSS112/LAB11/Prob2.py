def Problem2():
    return [sum([j for j in range(i,i+10) if j%2==1]) for i in range(1,99,10)]
