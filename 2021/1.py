# How many measurements are larger than the previous measurement?
input_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
print(sum([1 if input_list[x] > input_list[x-1] else 0 for x in range(1, len(input_list))]))
