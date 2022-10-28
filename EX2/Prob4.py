from functools import reduce

def p4():
  list_x = [1.5,2,0.5,4,5]
  fx = lambda x1,x2: (x2-x1)/(x2+x1)
  no4_ans = reduce(fx,list_x)
  return no4_ans