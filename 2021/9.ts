/*
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
*/

const heightMapString = `2199943210
3987894921
9856789892
8767896789
9899965678`

const isDefined = (x: any) : boolean => x !== undefined
const range = (n: number) => [...Array(n).keys()]
const addOne = (n: number) => n + 1
const sum = (accumulator: number, nextValue: number) => accumulator + nextValue

const toNumber = (n: string) => parseInt(n, 10)
const stringToNumberArray = (s: string) => [...s].map(toNumber)
const heightMap = heightMapString.split('\n').map(stringToNumberArray)
const columns = heightMap[0].length
const rows = heightMap.length

type Index = {row: number, col: number}
const valueAt = ({row, col}: Index) => heightMap[row][col]
const above = ({row, col}: Index) => row > 0 ? heightMap[row-1][col] : undefined
const below = ({row, col}: Index) =>  row < rows - 1 ? heightMap[row+1][col] : undefined
const left = ({row, col}: Index) => col > 0 ? heightMap[row][col-1] : undefined
const right = ({row, col}: Index) => col < columns - 1 ? heightMap[row][col+1] : undefined
const adjecentPoints = (index: Index) : number[] =>
    [above, below, left, right]
        .map(fn => fn(index))
        .filter(isDefined) as number[]
const pointHigher = (index: Index) => (n: number) =>
    valueAt(index) < n
const isLowest = (index: Index) =>
    adjecentPoints(index).every(pointHigher(index))

const indexes = range(rows)
    .flatMap(row => range(columns).map(col => ({row, col})))
const solution = indexes
    .filter(isLowest)
    .map(valueAt)
    .map(addOne)
    .reduce(sum, 0)

console.log(solution)