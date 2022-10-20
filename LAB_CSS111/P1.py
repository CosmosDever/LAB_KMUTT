def myreplace(str,old,new):
    res=''
    skip=0
    for i in range(len(str)):
        if skip:
            skip -= 1
            continue
        if str[i:i+len(old)]==old:
            res+=new
            skip=len(old)-1
        else:
            res+=str[i]             
    return res    
str = input()
old = input()
new = input()
print(myreplace(str,old,new))
    