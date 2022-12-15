#1.4 Problem
def Problem1_4(purchase_list):
    icecream_price_dict = {'cone':300, 'sherbet':200, 'choco': 100}
    total_purchase={}
    for item in purchase_list:
        if item in icecream_price_dict:
            item_price = int(icecream_price_dict[item])
            if item in total_purchase:
                total_purchase[item] += item_price
            else:
                total_purchase[item] = item_price
        else:
            total_purchase[item] = 0
    return total_purchase