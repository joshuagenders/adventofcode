# Determine the horizontal position that the crabs can align to using the least fuel possible.
# How much fuel must they spend to align to that position?
values = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
sum_abs_diff = []
# consider only occupied positions
for index, number in enumerate(values):
    sum_abs_diff.append(sum([abs(x - number) for x in values]))
result = min(sum_abs_diff)
desired_hposition = values[sum_abs_diff.index(result)]
print(result)
print(desired_hposition)

# consider every possible position
sum_abs_diff = []
min_value = min(values)
for number in range(min_value, max(values) + 1):
    sum_abs_diff.append(sum([abs(x - number) for x in values]))
result = min(sum_abs_diff)
desired_hposition = min_value + sum_abs_diff.index(result)
print(result)
print(desired_hposition)
