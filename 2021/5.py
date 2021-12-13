values = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

parsed = list(
    map(
        lambda x: list(map(
            lambda y: list(map(
                int,
                y.split(',')
            )),
            x.split(' -> ')
        )),
        values.splitlines()
    )
)
points = {}
for start, finish in parsed:
    x, y = start
    x2, y2 = finish
    if x == x2:
        inc = 1 if y2 > y else -1
        for n in range(y, y2 + inc, inc):
            key = (x, n)
            if key in points:
                points[key] += 1
            else:
                points[key] = 1
    elif y == y2:
        inc = 1 if x2 > x else -1
        for n in range(x, x2 + inc, inc):
            key = (n, y)
            if key in points:
                points[key] += 1
            else:
                points[key] = 1
print(len(list(filter(lambda v: v[1] > 1, points.items()))))

