import math

def is_prime(num):
  if (num == 1 or num ==2):
    return True

  i = 2
  while i <= math.sqrt(num):
    if is_prime(i) and num % i == 0:
      return False
    i += 1
  
  return True

def find_prime_factors(num):
  print(f'you passed type {type(num)}')

  if type(num) != int or num < 1:
    print("pass only positive itegers to the function")
    return
  
  if is_prime(num):
    return num
  

  

# find_prime_factors("string")
print(is_prime(17))
print(is_prime(18))
print(is_prime(19))
print(is_prime(20))
print(is_prime(45))

