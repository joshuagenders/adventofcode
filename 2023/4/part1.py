with open('data.txt', 'r') as fh:
  input_raw = fh.read()

# input_raw = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# '''

total = 0
x = [
  map(
    lambda n: set(filter(bool, n.strip().split(' '))),
    w[1].split('|')
  ) for w in [
    y.split(':') for y in input_raw.splitlines()
  ]
]
for a in x:
  b = list(a)
  print(b)
  l = len(b[0] & b[1])
  if l == 1:
    total += 1
  elif l > 1:
    total += 2 ** (l - 1)
  
print(total)