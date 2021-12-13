values = [16,1,2,0,4,2,7,1,2,14]
sum_abs_diff = []
for index, number in enumerate(values):
    list_without_number = values[:index] + values[index+1:]
    sum_abs_diff.append(sum([abs(x - number) for x in list_without_number]))
result = min(sum_abs_diff)
desired_hposition = values[sum_abs_diff.index(result)]
print(result)
print(desired_hposition)
