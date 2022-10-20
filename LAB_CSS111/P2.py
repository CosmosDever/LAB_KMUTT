num=input()
st=0
res='True'
for i in range(len(num)):
    if i > 0 and st==0:
        if int(num[i]) > int(num[i-1]):
            st=1
            continue
        elif int(num[i]) < int(num[i-1]):
            st=2 
            continue   
    if st == 1 and int(num[i]) > int(num[i-1]):
        res="False"
        break
    elif st == 1 and int(num[i]) < int(num[i-1]):
        st=0
    if st == 2 and int(num[i]) < int(num[i-1]):
        res="False"
        break
    elif st == 1 and int(num[i]) > int(num[i-1]):
        st=0  
print(res)                        
        
                
            
