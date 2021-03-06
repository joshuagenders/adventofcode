const text = `be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce`;

const uniqueLengths = (words: string[]) => {
    const lengths = words
        .map(word => word.length)
    return lengths.filter(l => lengths.filter(r => r === l).length === 1)
}

const parser = (line: string) : {combinations: string[], output: string[]} => {
    const values = line
        .split('|')
        .map(v => v.trim())
    return {
        combinations: values[0].split(' '),
        output: values[1].split(' ')
    }
}

const parsed = text.split("\n").map(parser)
const sumOfUniqueCombinations = parsed.map(line => {
    const counts = uniqueLengths(line.combinations)
    const countOfUnique = line.output.filter(o => counts.includes(o.length)).length
    return countOfUnique
}).reduce((acc, v) => acc + v, 0)
console.log(sumOfUniqueCombinations)
