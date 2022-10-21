from functools import reduce
def Problem2(atext):
    ltext = atext.split(" ")
    def relace_the_reduce(a,b):
        if a.lower()=='the':
            a='xxx'   
        if b.lower()=='the':
            b='xxx'        
        return a+' '+b
    anstext=reduce(relace_the_reduce,ltext)
    return anstext

