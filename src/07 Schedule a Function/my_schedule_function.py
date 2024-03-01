import time

def schedule_function(gotime, callback, *args):
  # print(f'go time is {int(gotime)}')
  while True:
    current_time = int(time.time())
    # print(f'current time is {current_time}')
    if current_time == int(gotime):
      break

    time.sleep(1)

  callback(*args)


schedule_function(time.time() + 1, print, 'Howdy!')