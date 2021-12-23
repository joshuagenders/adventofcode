var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
var text = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\nedbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\nfgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\nfbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\naecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\nfgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\ndbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\nbdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\negadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\ngcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce";
var uniqueLengths = function (words) {
    return words
        .map(function (word) { return word.length; })
        .reduce(function (acc, wordLength) { return acc.includes(wordLength)
        ? acc.filter(function (w) { return w !== wordLength; })
        : __spreadArray([wordLength], acc, true); }, []);
};
var parser = function (line) {
    return line.split('|').map(function (v) { return v.trim(); }).map(function (l) { return l.split(' '); });
};
var parsed = text.split("\n").map(parser);
var sumOfUniqueCombinations = parsed.map(function (line) {
    var combinations = line[0];
    var output = line[1];
    var counts = uniqueLengths(combinations);
    var countOfUnique = output.filter(function (o) { return counts.includes(o.length); }).length;
    return countOfUnique;
}).reduce(function (acc, v) { return acc + v; }, 0);
console.log(sumOfUniqueCombinations);
