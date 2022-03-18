# The submarine has a bingo subsystem to help passengers
# (currently, you and the giant squid) pass the time.
# Start by finding the sum of all unmarked numbers on that board.
# Then, multiply that sum by the number that was just called when the board won to get the final score.
# To guarantee victory against the giant squid, figure out which board will win first.
# What will your final score be if you choose that board?

board_text = """
22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17 5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
boards = []
current_board = []
board_sum = 0
board_sums = []
for line in board_text.splitlines():
    line_values = list(filter(lambda x: x != '', line.split(' ')))
    if not line_values:
        if current_board:
            boards.append(current_board)
            board_sums.append(board_sum)
        current_board = []
        board_sum = 0
    else:
        values = list(map(int, line_values))
        current_board.append(values)
        board_sum += sum(values)
if current_board:
    boards.append(current_board)
    board_sums.append(board_sum)
numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
           16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

print('boards')
print(boards)

print('board sums')
print(board_sums)

# key = number, value = board, x, y
tables = {}
sums = []
# todo - build this during board parsing...
for board_index, board in enumerate(boards):
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            key = boards[board_index][row_index][column_index]
            if key not in tables:
                tables[key] = [(board_index, row_index, column_index)]
            else:
                tables[key].append((board_index, row_index, column_index))
print(tables)

scores = {}
def row_key(board, row): return (board, 'row', row)
def col_key(board, col): return (board, 'col', col)


def mark(board, row, col):
    r_key = row_key(board, row)
    c_key = col_key(board, col)
    if r_key in scores:
        scores[r_key] += 1
        if scores[r_key] >= 5:
            return True
    else:
        scores[r_key] = 1
    if c_key in scores:
        scores[c_key] += 1
        if scores[c_key] >= 5:
            return True
    else:
        scores[c_key] = 1
    return False


winners = []
winning_turn = 0
for turn, number in enumerate(numbers):
    if not number in tables:
        continue
    for board, x, y in tables[number]:
        print(f'number: {number} board: {board} x={x} y={y}')

        board_sums[board] -= number
        won = mark(board, x, y)
        if won:
            winners.append((board, number))
    if winners:
        winning_turn = turn
        break
print(winners)
print(*[f'board {winner}, winning_number: {winning_number}, remaining sum: {board_sums[winner]}, turn: {winning_turn}, score: {winning_number * board_sums[winner]}' for winner, winning_number in winners])
