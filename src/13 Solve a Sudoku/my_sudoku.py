from itertools import product

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def print_sudoku(puzzle):
    # replace zeroes with dashes
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0, 9):
        if ((row % 3 == 0) and (row != 0)):
            print('-' * 33)  # draw horizontal line
        for col in range(0, 9):
            if ((col % 3 == 0) and (col != 0)):
                print(' | ', end='')  # draw vertical line
            print(f' {puzzle[row][col]} ', end='')
        print()
    print()


def is_in_line(row, col, num, puzzle):
  for i in range(0,9):
    if num in (puzzle[i][col], puzzle[row][i]):
      return True
    
  return False


def is_in_section(row, col, num, puzzle, size=3):
  for (i, j) in product(range(0, size), repeat=2):
    box_row = row - row % size + i
    box_col = col - col % size + j
    if puzzle[box_row][box_col] == num:
      return True
    
  return False
  

def is_num_allowed(row, col, num, puzzle):

  if is_in_line(row, col, num, puzzle):
    return False
  
  if is_in_section(row, col, num, puzzle, 3):
    return False

  return True
    

def get_possible_numbers(puzzle):
  cells_to_fill = {}

  for (row, col) in product(range(0,9), repeat=2):
      
      if puzzle[row][col] == 0:
        cell = (row, col)
        cells_to_fill[cell] = []
        for num in range(1, 10):
            if is_num_allowed(row, col, num, puzzle):
              cells_to_fill[cell].append(num)
  return cells_to_fill


def solve_sudoku(puzzle):
  for (row, col) in product(range(0,9), repeat=2):
  
    if puzzle[row][col] == 0:

      for num in range(1, 10):
        if is_num_allowed(row, col, num, puzzle):
          puzzle[row][col] = num

          trial = solve_sudoku(puzzle)
          if trial:
            return trial
          puzzle[row][col] = 0

      return False
    
  return puzzle

def my_solve_sudoku(puzzle):
  cells_to_fill = get_possible_numbers(puzzle)

  for (row, col) in list(cells_to_fill.keys()):
    possible_numbers = cells_to_fill[(row, col)]
    for num in possible_numbers:
        puzzle[row][col] = num
        trial = my_solve_sudoku(puzzle)
        if trial:
          return trial
        puzzle[row][col] = 0

    return False
  return puzzle




# solved_puzzle = solve_sudoku(puzzle)
# print_sudoku(solved_puzzle)
    
solved = my_solve_sudoku(puzzle)
print_sudoku(solved)
    
