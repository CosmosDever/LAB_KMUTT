#1
c=int(input('Please enter the temperature in Celsiu:'));print(f'The {"%.1f" % c} Celcius = {"%.1f" % ((9/5)*c+32)} Farenhite')
#2
Num=int(input('Enter number '))
def Summationt(n):
    if n==0:
        return 0
    else: return n+Summationt(n-1)
print(f'Summation of numbers from 1 to {"%.0f" % Num} is: {"%.0f" % Summationt(Num)}')
#3
Num=int(input('Enter a number to to make a multiplication table: '))
for i in range(Num):
    print(Num,'x',i+1,'=',(i+1)*Num)
#4
scores=int(input('Please enter your score: '))
def determine_grade(scores):
    if scores >= 80 and scores<= 100:
        return 'A'
    elif scores >= 75 and scores<= 79:
        return 'B+'
    elif scores >= 70 and scores<= 74:
        return 'B'
    elif scores >= 65 and scores<= 69:
        return 'C+'
    elif scores >= 60 and scores<= 64:
        return 'C'
    elif scores >= 55 and scores<= 59:
        return 'D+'
    elif scores >= 50 and scores<= 54:
        return 'D'
    else:
        return 'F'
print('You got',determine_grade(scores))
#5
start,stop=int(input('Please enter a starting number:')),int(input('Please enter a ending number:'))
print(f'Prime numbers between {"%.0f"%start} and {"%.0f"%stop} are: ')
for i in range(start,stop+1):
   if i > 1:
       for n in range(2, i):
           if (i % n) == 0:
               break
       else:print(i)