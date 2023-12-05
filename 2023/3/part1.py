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

# [{n: 123, locations: [x,y]}]
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
      locations.append([x,y])
    else:
      if num:
        numbers.append({'number': int(num), 'locations': locations})
        num = ""
        locations = []
      if not c == '.':
        symbols[f'{x},{y}'] = c
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
for number in numbers:
  is_valid = False
  for [x, y] in number['locations']:
    for adjecent in adjecent_locations(x, y):
      if adjecent in symbols:
        is_valid = True
        break
    if is_valid:
      break
  if is_valid:
    total += number['number']

print(total)