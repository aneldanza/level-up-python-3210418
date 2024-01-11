import string

def count_words(file_path):
  with open(file_path, 'r') as f:
    text = f.read()
    words = text.split()
    print(f'there are {len(words)} words in the file.')

  punctuation = ['.',':', '?', '!','%','*','^','(', ')','-','<','>','"','{','}','[',']','|','\\']
  dict = {}

  for word in words:
    word = word.translate('', '', string.punctuation)
    if dict[word.lower()]:
      dict[word.lower()] += 1
    else:
      dict[word.lower()] = 1
      
  pairs = dict.items()
  sorted_dict = sorted(pairs, key=lambda x=x[1])