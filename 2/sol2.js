const input_list = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

const match = (val) => ({
    when: (regx, fn) => regx.test(val) ? matched(fn(val)) : match(val),
    otherwise:(fn) => fn(val)
})
const matched = (val) => ({
    when: () => matched(val),
    otherwise: () => val
})

const getAmount = val => parseInt(val.split(' ')[1], 10)
// apply transformations to [horizontalPosition, depth] vector
const forward = acc => v => [acc[0] + getAmount(v), acc[1]] 
const down = acc => v => [acc[0], acc[1] + getAmount(v)] 
const up = acc => v => [acc[0], acc[1] - getAmount(v)] 

const [horizontalPosition, depth] = input_list.reduce((acc, v) => match(v)
    .when(/forward/, forward(acc))
    .when(/down/, down(acc))
    .when(/up/, up(acc))
    .otherwise(() => acc), [0, 0])

console.log({horizontalPosition, depth})
console.log(horizontalPosition * depth)

