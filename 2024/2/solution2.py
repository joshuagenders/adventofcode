contents = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

with open("input.txt") as f:
    contents = f.read()

lines = filter(lambda x: x != "", contents.splitlines())
parsed = [list(map(int, line.split())) for line in lines]
diffs = list([
    [line[i] - line[i+1] for i in range(len(line) - 1)] for line in parsed
])
lt3 = lambda x: x <= 3
gtn3 = lambda x: x >= -3
is_positive = lambda x: x > 0
is_negative = lambda x: x < 0

def is_valid(diff) -> bool:
    return all(map(is_positive, diff)) \
        and all(map(lt3, diff)) \
        or all(map(is_negative, diff)) \
        and all(map(gtn3, diff))

valid = sum(
    [
        1 for diff in diffs 
        if is_valid(diff)
    ]
)
print(valid)

v = 0
for line in parsed:
    reports = [line[0:i] + line[i+1:] for i in range(len(line))]
    diffs = list([
        [line[i] - line[i+1] for i in range(len(line) - 1)] for line in reports
    ])
    if any(map(is_valid, diffs)):
        v += 1
print(v)