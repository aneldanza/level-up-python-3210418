from random import randint
import time
import math

def waiting_game():
  seconds = randint(2, 4)
  print(f'Your target time is {seconds} seconds')
  print()
  input('--Press ENTER to begin\n')
 
  start = time.time()

  input(f'...Press ENTER again after {seconds} seconds ...\n')
  
  end = time.time()
  elapsed_time = end - start
  print(f'Elapsed time: {round(elapsed_time, 3)}')
  diff = abs(elapsed_time - seconds)
  if (elapsed_time > seconds):
    print(f'({round(diff, 3)} seconds too slow)')
  elif elapsed_time < seconds:
    print(f'({round(diff, 3)} seconds too fast)')
  else:
    print(f'Right on!')

waiting_game()