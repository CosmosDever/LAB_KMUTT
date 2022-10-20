#1
def Print_Name(n,l):
    def Get_Name():
        return n + ' ' + l
    print('Hi,',Get_Name()+'!')
First=input('What is your name?: ')
Last=input('What is your last name?: ')
Print_Name(First,Last)

#2
def Celcius_To_Farenheit(s,t):
    if s==t:
        return print(f'{s} Celsius = {"%.2f" % ((9 / 5) * s + 32)} Fahrenheit.')
    else:
        return print(f'{s} Celsius = {"%.2f" % ((9 / 5) * s + 32)} Fahrenheit.'),Celcius_To_Farenheit(s+1,t)
Start=int(input('Enter a beginning Celsius value: '))
Stop=int(input('Enter an ending Celsius value: '))
Celcius_To_Farenheit(Start,Stop)

#3
i=1
def Multiplication(n,i):
    if i>12:
        return
    else:
        return print(n,'X',i,'=',n*i),Multiplication(n, i + 1)
num=int(input('Enter a number: '))
print('Multiplication Table of',num,'is:')
Multiplication(num,i)

#4
L=['tony', 'peter', 'mark', 'kim', 'james','kenny']
Name=input('Please enter your name: ').lower()
Age=int(input('Please enter your age: '))
def Check_Member(n,a):
    def Check_Age(a):
        if a < 15:
            return 'kid'
        else:
            return 'notkid'
    if n in L:
        if Check_Age(a) == 'kid':
            return 15-(15*(75/100))
        elif Check_Age(a) == 'notkid':
            return 15-(15*(50/100))
    else:
        if Check_Age(a) == 'kid':
            return 15-(15*(50/100))
        elif Check_Age(a) == 'notkid':
            return 15
print('Ticket price for',Name.capitalize(),'is: $',f'{round(Check_Member(Name,Age),2)}')

