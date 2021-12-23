var text = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\nedbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\nfgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\nfbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\naecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\nfgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\ndbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\nbdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\negadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\ngcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce";
var uniqueLengths = function (words) {
    var lengths = words
        .map(function (word) { return word.length; });
    return lengths.filter(function (l) { return lengths.filter(function (r) { return r == l; }).length == 1; });
};
var parser = function (line) {
    return line.split('|').map(function (v) { return v.trim(); }).map(function (l) { return l.split(' '); });
};
var parsed = text.split("\n").map(parser);
var sumOfUniqueCombinations = parsed.map(function (line) {
    var combinations = line[0];
    var output = line[1];
    var counts = uniqueLengths(combinations);
    console.log(combinations);
    console.log(counts);
    console.log(output);
    var countOfUnique = output.filter(function (o) { return counts.includes(o.length); }).length;
    console.log(countOfUnique);
    console.log("===============");
    return countOfUnique;
}).reduce(function (acc, v) { return acc + v; }, 0);
console.log(sumOfUniqueCombinations);
