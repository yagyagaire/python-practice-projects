#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
import math

def prime_factors(n):
  factors = []
  while n % 2 == 0:
    if 2 not in factors:
      factors.append(2)
    n = n / 2
  
  #n must be odd by now, so we can start from 3 upto sqrt(n), with a step of 2.
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
      factors.append(int(i))
      n = n / i
  
  #if n is a prime number greater than 2, at this stage, it is a prime number. 
  if n > 2:
    if n not in factors:
      factors.append(int(n))
  return sorted(list(set(factors)))

print(prime_factors(1))
