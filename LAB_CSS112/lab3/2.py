#1
User = input("What is your name?:")
List = ['jeff','jack','jim']
def IsMyFrined(n):
    if n.lower() in List:
        return (f'Hello, {"%s"%n.capitalize()}. Good morning my frined!')
    else:return (f'Who are you?\nNice to meet you anyway...{"%s"%n.capitalize()} :).')
print(IsMyFrined(User))