contents = '''
3   4
4   3
2   5
1   3
3   9
3   3
'''.splitlines()

with open("input1.txt") as f:
    contents = list(map(lambda x: x.replace('\n', ''), f.readlines()))

remove_empty_lines = lambda lines: filter(lambda x: x != "", lines)
lines = remove_empty_lines(contents)
lines = [list(map(int, line.split("   "))) for line in lines]
index = lambda i: lambda list: list[i]
extract_column = lambda i, list: map(index(i), list)
extract_sorted_column = lambda i, list: sorted(extract_column(i, list))

left = extract_sorted_column(0, lines)
right = extract_sorted_column(1, lines)

diff = sum([abs(x[0] - x[1]) for x in zip(left, right)])
print (diff)

equality = lambda a: lambda b: a == b

total = 0
for n in left:
    times = len([x for x in filter(equality(n), right)])
    total += n * times

print(total)