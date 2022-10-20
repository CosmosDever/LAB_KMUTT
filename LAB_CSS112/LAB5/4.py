f = open("CelsiustoFahrenheit.txt", "w+")
def cal(s,st):
    if s<=st:
        f.write(f'{s} Celsius = {"%.2f"%(s*(9/5)+32)} Fahrenheit.\n')
        s+=1
        cal(s,st) 
begin=int(input('Enter a begining Celsius value: '))
ending=int(input('Enter a ending Celsius value: '))
cal(begin,ending)
f.close()