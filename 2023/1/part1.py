with open('data.txt', 'r') as fh:
  input_raw = fh.read()

# input_raw = '''1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet'''

total = 0
for line in input_raw.splitlines():
  num = ""
  for c in line:
    if c.isdigit():
      num += c
      break
  for c in reversed(line):
    if c.isdigit():
      num += c
      break
  total += int(num)
print(total)