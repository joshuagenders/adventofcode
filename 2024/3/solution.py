import re
# contents = '''
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# '''

contents = '''
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
'''

with open("input.txt") as f:
    contents = f.read()

def calculate(instruction) -> int:
    return sum([int(x[0])*int(x[1]) for x in re.findall("mul\((\d+),(\d+)\)", instruction, re.MULTILINE)])

result = calculate(contents)
print(result)

result2 = sum(
    map(calculate, 
        filter(lambda x: not x.startswith("n't"), contents.split("do"))
    )
)
print(result2)