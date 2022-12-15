# Question 3.1
def Problem3_1(max_prime = 1000):
    primes = [True] * (max_prime + 1)
    primes[0] = primes[1] = False
    for i in range(2, max_prime + 1):
        if primes[i]:
            for j in range(i * 2, max_prime + 1, i):
                primes[j] = False
    for i in range(2, max_prime + 1):
        if primes[i] and primes[i + 2]:
            yield (i, i + 2)
a=Problem3_1(35)            
for i in range(5):
    f= next(a)
    print(f)
                
