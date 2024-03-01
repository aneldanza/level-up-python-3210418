def sort_words(text):
  words = text.split()
  i = 0
  j = 0
  swapped = False

  while i < len(words) - 1:
    swapped = False
    j = 0
    while j < len(words) - i - 1:
      current = words[j]

      if current.lower() > words[j + 1].lower():
        words[j] = words[j + 1]
        words[j + 1] = current
        swapped = True
      
      j += 1
    
    if swapped == False:
      break
    i += 1
  
  return words

  
print(sort_words('banana ORANGE apple'))