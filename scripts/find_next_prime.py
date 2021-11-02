#Find prime numbers until stopped
import math

def is_prime(n):
  #Base case for prime numbers
  if n == 2 or n == 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  
  #Prime optimization algorithm, check if number is divisble by any odd numbers
  for i in range(5, int(math.sqrt(n)), 2):
    if n % i == 0:
      return False

  return True

def get_next_prime(n):
  while not is_prime(n):
    n = n + 1
  return n

res = input('Enter a number to find next closest prime (Enter "q" to quit): ')

while res.lower() != 'q':
  print(get_next_prime(int(res)), '\n')
  res = input('Enter a number to find next closest prime (Enter "q" to quit):')  
  