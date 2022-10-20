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
