with open('data.txt', 'r') as fh:
  input_raw = fh.read()

# input_raw = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# '''

games = map(
  lambda game: [
    int(game[0].replace('Game ', '')),
    map(
      lambda g: g.strip().split(','),
      game[1].split(';')
    )
  ],
  [line.split(':') for line in input_raw.splitlines()]
)
total = 0

for game in games:
  num_cubes = {
    'red': 0,
    'green': 0,
    'blue': 0
  }  
  for draw in game[1]:
    for colour in draw:
      [amount, c] = colour.strip().split(' ')
      if num_cubes[c] < int(amount):
        num_cubes[c] = int(amount)
  total += num_cubes['red'] * num_cubes['green'] * num_cubes['blue']
  
print(total)

# print(*result, sep="\n")