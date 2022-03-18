/*
Calculate the horizontal position and depth you would have after following the planned course.
What do you get if you multiply your final horizontal position by your final depth?
*/

const input_list = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

const result = input_list.reduce((acc, v) => {
    const match = v.match(/(?<direction>forward|down|up) (?<amount>\d*)/)
    if (match){
        const direction = match.groups['direction']
        console.log(direction)
        switch(direction.toLocaleLowerCase()){
            case "forward":
                acc[1] += parseInt(match.groups['amount'], 10)
                break;
            case "down":
                acc[0] += parseInt(match.groups['amount'], 10)
                break;
            case "up":
                acc[0] -= parseInt(match.groups['amount'], 10)
                if (acc[0] < 0){
                    acc[0] = 0
                }
                break;
            default:
                console.log(`unknown direction ${direction}`)
        }
    } else {
        console.log(`unknown command: ${v}`)
    }
    console.log(acc)
    return acc
}, [0, 0])

console.log(result[0] * result[1])