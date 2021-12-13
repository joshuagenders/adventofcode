# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
# then multiply them together. What is the power consumption of the submarine?
# (Be sure to represent your answer in decimal, not binary.)
input_list = [ '00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010' ]
transposed = [[val[bit_position] for val in input_list] for bit_position in range(5)]
most_common = int(''.join(['1' if val.count('1') > val.count('0') else '0' for val in transposed]), 2)
not_most_common = ~most_common & int('11111', 2)
print(most_common * not_most_common)
