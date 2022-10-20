#1
User = input("What is your name?:")
List = ['jeff','jack','jim']
def IsMyFrined(n):
    if n.lower() in List:
        return (f'Hello, {"%s"%n.capitalize()}. Good morning my frined!')
    else:return (f'Who are you?\nNice to meet you anyway...{"%s"%n.capitalize()} :).')
print(IsMyFrined(User))
#2
WorkHour = int(input("How many hours did you work last week? "))
money = 0
Rate = int(input("What is your pay rate per hour(between 10-25 ) "))
def GetMoney(n):
    if n <=40:
        money = n * Rate
        return money
    else:money=(40*Rate)+((n-40)*(Rate*1.5))
    return money
print(GetMoney(WorkHour))
#3
Num = int(input("Enter a number to test: "))
def IsPrime(n):
    for i in range(n):
        if i > 1:
            for n in range(2, i):
                if (i % n) == 0:
                    break
            else:
                return ("This is prime number")
print(IsPrime(Num))
#4
import math
Elements = int(input("Enter num of elements : "))
List = []
def AddlList(n):
    for i in range(n):
        List.append(int(input()))
    return List
print("The entered list is",AddlList(Elements))
print("The maximum number entered is",max(List))
print("The minimum number entered is",min(List))
#5
print("Please enter a choice for your selection:\nEnter 1 if you want to calculate the area of a triangle.\nEnter 2 if you want to calculate the volumn of a cubic.\nEnter 3 if you want to calculate the volumn of a cone.")
Choice = int(input("Enter your choice here: "))
def Area_Of_A_Triangle(n):
    if n == 1:
        Base=int(input("Please enter the base length: "))
        Height=int(input("Please enter the height: "))
        return (f'The area of a triangle with base = {"%.d"%Base} and height = {"%.d"%Height} is {"%.1f"%((1/2)*Base*Height)}')
def Volumn_Of_A_Cubic(n):
    if n == 2:
        Width=int(input("Please enter the base width: "))
        Length = int(input("Please enter the length: "))
        Height=int(input("Please enter the height: "))
        return (f'The volumn of a cubic with width = {"%.d"%Width} length = {"%.d"%Length} and height = {"%.d"%Height} is {"%.d"%(Width * Height * Length)}')
def Volumn_Of_A_Cone(n):
    if n == 3:
        BaseDiameter=int(input("Please enter the base diameter: "))
        Height=int(input("Please enter the height: "))
        return (f'The volumn of a cubic with basediameter = {"%.1f"%BaseDiameter} and height = {"%.1f"%Height} is {"%.1f"%(((3.14*((BaseDiameter/2)*(BaseDiameter/2)))*Height))}')
if Choice == 1:
    print(Area_Of_A_Triangle(Choice))
elif Choice == 2:
    print(Volumn_Of_A_Cubic(Choice))
elif Choice == 3:
    print(Volumn_Of_A_Cone(Choice))
