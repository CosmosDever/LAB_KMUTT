start,stop=int(input('Please enter a starting number:')),int(input('Please enter a ending number:'))
print(f'Prime numbers between {"%.0f"%start} and {"%.0f"%stop} are: ')
for i in range(start,stop+1):
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:print(i)
