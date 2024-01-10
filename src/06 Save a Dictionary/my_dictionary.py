import json

def save_dict(dict, filename):
  with open(filename, 'w') as f:
    json.dump(dict, f)

def load_dict(filename):
  with open(filename, 'r') as f:
    dict = f.read()
  
  return dict

dict = {1: 'a', 2: 'b', 3: 'c'}
save_dict(dict, 'test.txt')
print(load_dict('test.txt'))