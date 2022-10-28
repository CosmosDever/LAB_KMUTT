import math
def p3(a,b):
  while b != 0: 
    t = b;
    b = a%b;
    a = t;
  gcd = a;
  return gcd