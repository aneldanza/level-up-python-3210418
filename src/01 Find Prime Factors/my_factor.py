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

def get_next_prime(num):
  found_prime = 0
  i = 1

  while not found_prime:
    if is_prime(num + i):
      found_prime = num + i
      break
    i += 1
  
  return found_prime


def find_prime_factors(num):
  output = list()

  if type(num) != int or num < 1:
    print("pass only positive itegers to the function")
    return output

  next_prime = 2

  if is_prime(num):
    output.append(num)
  else:
    while num % next_prime > 0:
      next_prime = get_next_prime(next_prime)
    
    output.append(next_prime)
    remainder = int(num / next_prime)
    right = find_prime_factors(remainder)
    output.extend(right)
    
  return output
  

  

print(find_prime_factors(630))



