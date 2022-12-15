#Quesion 1.3 
def Problem1_3(purchase_list):
    icecream_price_dict = {'cone':'300', 'sherbet':'200', 'choco': '100'}
    return sum(int(icecream_price_dict[item]) if item in icecream_price_dict else 0 for item in purchase_list)
print(Problem1_3(['boba','boba','cone','choco','choco']))