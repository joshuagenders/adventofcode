raw_input = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

with open('10.input.txt', 'r') as fh:
    raw_input = fh.read()

x = 1
def add_x(v):
    def execute() -> int | None:
        yield 0
        yield v
        yield None
    return execute
def noop() -> int | None:
    yield 0
    yield None
def to_instr(instruction: str):
    i = instruction.split(' ')
    if len(i) == 1:
        return noop
    else:
        return add_x(int(i[1]))

signal_strength = 0

instruction_stack = list(map(to_instr, raw_input.splitlines()))

current_instruction = instruction_stack.pop(0)()
cycle = 0
# for cycle in range(1, 221):
while instruction_stack:
    cycle += 1
    dx = current_instruction.__next__()

    if dx is None:
        current_instruction = instruction_stack.pop(0)()
        dx = current_instruction.__next__()

    if (cycle - 20) % 40 == 0:
        print(f'cycle {cycle} x {x} st{cycle * x} dx {dx}')
        signal_strength += cycle * x
    x += dx
print(signal_strength)

## part 2
instruction_stack = list(map(to_instr, raw_input.splitlines()))

current_instruction = instruction_stack.pop(0)()
cycle = 0
# for cycle in range(1, 221):
screen_buffer = ''
while instruction_stack:
    cycle += 1
    dx = current_instruction.__next__()

    if dx is None:
        current_instruction = instruction_stack.pop(0)()
        dx = current_instruction.__next__()

    x += dx
    current_px = cycle % 40
    print(current_px)
    if current_px in [x-1, x, x + 1]:
        screen_buffer += '#'
    else:
        screen_buffer += '.'
    if current_px == 0:
        screen_buffer += '\n'

print(screen_buffer)