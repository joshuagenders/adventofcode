# raw_input = '''R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2'''

with open('9.input.txt', 'r') as fh:
    raw_input = fh.read()

visited = {}
hx=0
hy=0
x=0
y=0

for line in raw_input.splitlines():
    [direction, steps] = line.split(' ')
    steps = int(steps)
    # there is a much better way to do this...presumably with some vector math
    for step in range(steps):
        if direction == 'U':
            hy += 1
        if direction == 'D':
            hy -= 1
        if direction == 'L':
            hx -= 1
        if direction == 'R':
            hx += 1
        dx = abs(hx - x)
        dy = abs(hy - y)
        are_adjecent = (not (dx > 1 or dy > 1)) or (dx == 1 and dy == 1)
        # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
        if hx == x + 2 and hy == y:
            x += 1
        elif hx == x - 2 and hy == y:
            x -= 1
        elif hy == y + 2 and hx == x:
            y += 1
        elif hy == y - 2 and hx == x:
            y -= 1
        # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
        elif not are_adjecent:
            if hx > x:
                x += 1
            else:
                x -= 1
            if hy > y:
                y += 1
            else:
                y -= 1
        visited[f'{x},{y}'] = True
print(len(visited))

# raw_input = '''R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20'''

visited = {}
rope = [[0,0] for _ in range(10)] 
print(rope)
for line in raw_input.splitlines():
    [direction, steps] = line.split(' ')
    steps = int(steps)

    # there is a much better way to do this...presumably with some vector math
    for step in range(steps):
        for index, v in enumerate(rope):
            if index == 0:
                if direction == 'U':
                    v[1] += 1
                if direction == 'D':
                    v[1] -= 1
                if direction == 'L':
                    v[0] -= 1
                if direction == 'R':
                    v[0] += 1
                continue
            x = v[0]
            y = v[1]
            hx = rope[index -1][0]
            hy = rope[index -1][1]
            dx = abs(hx - x)
            dy = abs(hy - y)
            are_adjecent = (not (dx > 1 or dy > 1)) or (dx == 1 and dy == 1)
            # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
            if hx == x + 2 and hy == y:
                x += 1
            elif hx == x - 2 and hy == y:
                x -= 1
            elif hy == y + 2 and hx == x:
                y += 1
            elif hy == y - 2 and hx == x:
                y -= 1
            # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
            elif not are_adjecent:
                if hx > x:
                    x += 1
                else:
                    x -= 1
                if hy > y:
                    y += 1
                else:
                    y -= 1
            rope[index][0] = x
            rope[index][1] = y
            if index == 9:
                visited[f'{x},{y}'] = True

print(len(visited))


