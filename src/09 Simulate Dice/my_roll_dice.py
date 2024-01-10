import random

def roll_dice(*args):
  max = 0 
  min = len(args)
  for sides in args:
    max += sides
  
  variations = list(range(min, max + 1))
  print(variations)

  i = 0
  dict = {var: 0 for var in variations}
  number_of_rolls = 1000000
  while i < number_of_rolls:
    outcome = sum(random.randint(1, sides) for sides in args)
    dict[outcome] += 1
    i += 1

  print(dict)

  for key, value in dict.items():
    percentage = round(value/number_of_rolls, 4)
    dict[key] = percentage
    print(f'{key}\t{percentage}%')

  

roll_dice(4, 6, 6)