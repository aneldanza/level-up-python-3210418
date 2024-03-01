import secrets

def generate_passphrase(word_count):
  with open('diceware.wordlist.asc', 'r') as f:
    lines = f.readlines()[2:7778]
    words = [line.split()[1] for line in lines]

  phrase_array = []

  for _ in range(0,word_count):
    phrase_array.append(secrets.choice(words))

  return ' '.join(phrase_array)

print(generate_passphrase(4))
  
