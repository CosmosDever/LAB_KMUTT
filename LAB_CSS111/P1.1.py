def myreplace(words,old,new):
    res=''
    i=0
    flags=0
    while i < len(words):
        if words[i:i+len(old)] == old:
            res+=new
            flags+=1 
            i+=len(old)
        res+=words[i]
        i+=1
    ans=res+'\n'+str(flags)
    return ans
words = input()
old = input()
new = input()
print(myreplace(words,old,new))