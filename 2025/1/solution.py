from functools import reduce
from math import floor


contents = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

with open("input.txt") as f:
    contents = f.read()

lines = [[x[0], int(x[1:])] for x in contents.splitlines()]
pos = 50
score = 0
print(lines)
for [direction, amount] in lines:
    if direction == "L":
        pos = pos - amount
        pos = pos % 100
        print({ "direction": direction, "amount": amount, "pos": pos})
    if direction == "R":
        pos = pos + amount
        pos = pos % 100
        print({ "direction": direction, "amount": amount, "pos": pos})
    if pos == 0:
        score += 1
print(score)

op = lambda direction: lambda a, b: (a - b) % 100 if direction == "L" else (a + b) % 100 
results = len(
    list(
        filter(lambda x: x == 0,
            reduce(
                lambda acc, v: acc + [op(v[0])(acc[-1], v[1])],
                lines,
                [50]
            )
        )
    )
)
print(results)

# part 2
print("=======")
pos = 50
score = 0

for [direction, amount] in lines:
    p = f"The dial is rotated {direction}{amount}"
    n = 0
    start_at_0 = pos == 0
    if direction == "L":
        pos -= amount
        if pos == 0:
            n += 1
        if pos < 0:
            n += floor(abs(pos) / 100) + 1
            if start_at_0:
                n -= 1
        pos = pos % 100
        p += f" to point at {pos}"
        if n > 0:
            p += f"; during this rotation, it points at 0 once."

    if direction == "R":
        pos += amount
        if pos == 100:
            n += 1
        if pos > 100:
            n += floor(abs(pos) / 100)
        pos = pos % 100
        p += f" to point at {pos}"
        if n > 0:
            p += f"; during this rotation, it points at 0 once."
    score += n

    print (p)
print(score)

# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
# The dial is rotated L30 to point at 52.
# The dial is rotated R48 to point at 0.
# The dial is rotated L5 to point at 95.
# The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
# The dial is rotated L55 to point at 0.
# The dial is rotated L1 to point at 99.
# The dial is rotated L99 to point at 0.
# The dial is rotated R14 to point at 14.
# The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
