contents = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

contents = '''
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
'''

with open("input.txt") as f:
    contents = f.read()

contents = list(filter(lambda x: x != "", contents.splitlines()))
get = lambda x, y: contents[y][x] if (x < len(contents[0]) and x >= 0 and y < len(contents) and y >= 0) else None
matrix = [
    [(0,1),(0,2),(0,3)], #downwards
    [(0,-1),(0,-2),(0,-3)], #upwards
    [(1,0),(2,0),(3,0)], #forwards
    [(-1,0),(-2,0),(-3,0)], #backwards
    [(1,1),(2,2),(3,3)], #se
    [(-1,-1),(-2,-2),(-3,-3)], #nw
    [(-1,1),(-2,2),(-3,3)], #sw
    [(1,-1),(2,-2),(3,-3)] #ne
]

count = 0
for y, line in enumerate(contents):
    for x, c in enumerate(line):
        if c == "X":
            for translation in matrix:
                m = get(x+translation[0][0], y+translation[0][1])
                a = get(x+translation[1][0], y+translation[1][1])
                s = get(x+translation[2][0], y+translation[2][1])
                if m == "M" and a == "A" and s == "S":
                    count += 1
print(count)

count = 0
for y, line in enumerate(contents):
    for x, c in enumerate(line):
        if c == "A":
            nw = get(x-1, y-1)
            se = get(x+1, y+1)
            ne = get(x+1, y-1)
            sw = get(x-1, y+1)
            
            if nw == "M" and se == "S" or nw == "S" and se == "M":
                if ne == "M" and sw == "S" or ne == "S" and sw == "M":
                    count += 1
print(count)