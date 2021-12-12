const input_list = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

const match = (val) => ({
    when(regx, fn){
        return regx.test(val) ? matched(fn(val)) : match(val)
    },
    otherwise(fn){
        return fn(val)
    }
})
const matched = (val) => ({
    when(){
        return matched(val)
    },
    otherwise(){
        return val
    }
})

const getAmount = val => parseInt(val.split(' ')[1], 10)
const forward = acc => v => { acc[0] += getAmount(v); return acc; } 
const down = acc => v => { acc[1] += getAmount(v); return acc;  } 
const up = acc => v => { acc[1] -= getAmount(v); return acc;  } 

const result = input_list.reduce((acc, v) => match(v)
    .when(/forward/, forward(acc))
    .when(/down/, down(acc))
    .when(/up/, up(acc))
    .otherwise(() => acc), [0, 0])

console.log(result)
console.log(result[0] * result[1])

