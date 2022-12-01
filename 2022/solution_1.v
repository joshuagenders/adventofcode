import arrays
input := (
	'
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
	'
)

values := input.split_into_lines()
mut elf_calories := [0]
for item in values {
	if item != '' {
		elf_calories[elf_calories.len - 1] += item.int()
	} else {
		elf_calories << 0
	}
}
elf_with_most_calories := arrays.max(elf_calories)!
println(elf_with_most_calories)