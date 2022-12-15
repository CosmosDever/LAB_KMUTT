# Problem 5
def Problem5():
    tester =[4,'5',0,'aa',0.2]
    msg = []
    for i in tester:
        try:
            num = int(i)
            if num % 2 != 0:
                raise ValueError("Not an even number!")
            reciprocal = 1/num
        except ValueError as ve:
            msg.append(str(ve))
        except ZeroDivisionError as ze:
            msg.append(str(ze))        
        else:    
            msg.append(reciprocal)
            
    adict = {'key1':10,'key2':20}
    try:
        adict['key3']
    except KeyError as ke:
        msg.append(str(ke))
    return msg