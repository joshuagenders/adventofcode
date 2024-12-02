contents = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

with open("input.txt") as f:
    contents = f.read()

def report_is_valid(report) -> bool:
    previous = None
    asc = None
    valid = True
    for n in report:
        if previous is None:
            previous = n
            continue

        diff = previous - n
        abs_diff = abs(diff)
        if abs_diff < 1 or abs_diff > 3:
            valid = False
            break
        if diff < 0:
            # asc
            if asc is None:
                asc = True
            if asc == False:
                valid = False
                break
        if diff > 0:
            if asc is None:
                asc = False
            if asc == True:
                valid = False
                break
        previous = n
    return valid

valid_reports = 0
for line in contents.splitlines():
    if line == "":
        continue
    report = map(int, line.split())
    valid = report_is_valid(report)
    if valid:
        valid_reports += 1

print(valid_reports)

valid_reports = 0
for line in contents.splitlines():
    if line == "":
        continue
    original_report = list(map(int, line.split()))
    reports = [original_report[0:i] + original_report[i+1:] for i in range(len(original_report))]
    for report in reports:
        valid = report_is_valid(report)
        if valid:
            valid_reports += 1
            break
print(valid_reports)