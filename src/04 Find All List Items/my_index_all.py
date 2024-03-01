

def index_all(input, value):
  output = []
  for index, el in enumerate(input):
    if el == value:
      output.append([index])
    elif isinstance(el, list):
      nested_result = index_all(el, value)
      for array in nested_result:
        output.append([index] + array)

  return output

example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# print(index_all(example, [1, 2, 3]))
print(index_all(example, 2))
# [[0, 0, 1], [0, 1], [1, 1]]