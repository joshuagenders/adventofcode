with open('data.txt', 'r') as fh:
  input_raw = fh.read()

# input_raw = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# '''

# [{n: 123, locations: ['x,y']]
# list as same part number can be counted more than once
numbers = []
# x,y: bool
symbols = {}

lines = input_raw.splitlines()
for y, line in enumerate(lines):
  num = ""
  locations = []
  for x, c in enumerate(line):
    if c.isdigit():
      num += c
      locations.append(f'{x},{y}')
    else:
      if num:
        numbers.append({'number': int(num), 'locations': locations})
        num = ""
        locations = []
      if c == '*':
        symbols[f'{x},{y}'] = [x, y]
  if num:
    numbers.append({'number': int(num), 'locations': locations})


def adjecent_locations(x: int, y: int):
  return [
    f'{x-1},{y}',
    f'{x+1},{y}',
    f'{x},{y-1}',
    f'{x},{y+1}',
    f'{x-1},{y-1}',
    f'{x+1},{y+1}',
    f'{x-1},{y+1}',
    f'{x+1},{y-1}',
  ]

total = 0
for [x, y] in symbols.values():
  adj_numbers = []
  adj = set(adjecent_locations(x, y))
  for num in numbers:
    if set(num['locations']) & adj:
      adj_numbers.append(num['number'])
  if len(adj_numbers) == 2:
    total += adj_numbers[0] * adj_numbers[1]  

print(total)