import math

def clean_letters(string):
  
  clean = []
  for ch in string:
    if ch.isalpha():
      clean.append(ch.lower())

  return "".join(clean)

def is_palindrome(string):

  chars = [ch.lower() for ch in string if ch.isalpha()]

  i = 0
  j = -1
  mid = math.floor(len(chars) / 2)
  
  while i < mid or j >= mid:
    if chars[i] != chars[-(i + 1)]:
      return False
    i += 1

  return True

print(is_palindrome("anela"))
print(is_palindrome("race car"))
print(is_palindrome("Go hang a salami, I’m a lasagna hog."))
