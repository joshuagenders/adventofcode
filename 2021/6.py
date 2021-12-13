initial_state = [ 3, 4, 3, 1, 2 ]

queue = []
for number in range(0, 9):
    queue.append(initial_state.count(number))

days = 80
for day in range(days):
    current_day = queue.pop(0)
    queue.append(current_day)
    queue[6] += current_day
print(sum(queue))
