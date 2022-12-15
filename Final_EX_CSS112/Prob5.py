# Problem 5
def Problem5():
    tester =[4,'5',0,'aa',0.2]
    msg = []
    for i in tester:
        #Your code here: try
            num = int(i)
            if num % 2 != 0:
                raise ValueError("Not an even number!")
            reciprocal = 1/num
        #Your code here: Exception value error as ve
            msg.append(str(ve))
        #Your code here: Zero devision error as ze
            msg.append(str(ze))        
        else:    
            msg.append(reciprocal)
            
    adict = {'key1':10,'key2':20}
    #Your code here: try
        adict['key3']
    #Your code here: Exception value error as ke
        msg.append(str(ke))
    return msg