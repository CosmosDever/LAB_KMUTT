def Problem3(N):
  primes = [i for i in range(1,N) if i not in [num for num in range(1,N) for d in range(2,num) if num%d == 0] ] 
  odd_dict_of_primes =  {k:v for (k,v) in dict(zip(range(len(primes)),primes)).items() if k%2 } 
  return odd_dict_of_primes