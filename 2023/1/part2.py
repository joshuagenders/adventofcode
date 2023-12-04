with open('data.txt', 'r') as fh:
  input_raw = fh.read()

# input_raw = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# '''

numbers = [
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
]

total = 0
for line in input_raw.splitlines():
  num = ""
  buffer = ""
  for c in line:
    if c.isdigit():
      num += c
      break
    else:
      buffer += c
      for i, n in enumerate(numbers):
        if n in buffer:
          num += str(i+1)
      if num:
        break
      
  buffer = ""
  last = ""
  for c in reversed(line):
    if c.isdigit():
      num += c
      break
    else:
      buffer = c + buffer
      for i, n in enumerate(numbers):
        if n in buffer:
          last += str(i+1)
      if last:
        num += last
        break
  if (num):
    total += int(num)
print(total)