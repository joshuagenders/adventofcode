contents = '''
3   4
4   3
2   5
1   3
3   9
3   3
'''

with open("input1.txt") as f:
    contents = f.read()

l = []
r = []
for line in filter(lambda x: x != "", contents.split("\n")):
    s = [ x for x in line.split("   ") if len(x) > 0]
    l.append(s[0])
    r.append(s[1])
l.sort()
r.sort()

combined = zip(l, r)
diffs = sum([abs(int(x[0]) - int(x[1])) for x in combined])
print (diffs)

m = {}
def identity(a):
    def id(b):
        return a == b
    return id

total = 0
for n in l:
    times = len([x for x in filter(identity(n), r)])
    total += int(n) * times
    # print (f'{n} appears {times} times')

print(total)