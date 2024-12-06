#!/usr/bin/python3

import copy

data = ''

lines = ''
with open(f'../Input/02.txt', 'r') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    new_lines.append(line[:-1])
lines = new_lines

def checkForJump(line):
    number = line[0]
    original = copy.deepcopy(line)
    result = True
    problem_index = 0

    first_result = True
    second_result = True

    for index, element in enumerate(line):
        if index == 0:
            continue
        difference = int(number) - int(line[index])
        number = line[index]

        if difference > 0:
            problem_index = index - 1
            result = False
            break

    if result == False:
        del line[problem_index]

        number = line[0]

        result = True

        # Test it again
        for index, element in enumerate(line):
            if index == 0:
                continue
            difference = abs(int(number) - int(line[index]))
            number = line[index]

            if difference > 3 or difference <= 0:
                first_result = False
                break
    else:
        first_result = True




    # Again!
    line = original
    problem_index = 0
    line.reverse()
    number = line[0]

    for index, element in enumerate(line):
        if index == 0:
            continue
        difference = int(number) - int(line[index])
        number = line[index]

        if difference > 0:
            problem_index = index
            result = False
            break

    if result == False:
        del line[problem_index]

        result = True
        number = line[0]

        # Test it again
        for index, element in enumerate(line):
            if index == 0:
                continue
            difference = abs(int(number) - int(line[index]))
            number = line[index]

            if difference > 3 or difference <= 0:
                second_result = False
                break
    else:
        second_result = True

    if first_result or second_result:
        return True
    else:
        return False



def checkForConsistency(line):
    number = line[0]
    original = copy.deepcopy(line)
    result = True
    problem_index = 0
    first_result = True
    second_result = True

    for index, element in enumerate(line):
        if index == 0:
            continue
        if int(line[index]) > int(number):
            number = int(line[index])
        else:
            problem_index = index - 1
            result = False
            break

    if not result:
        del line[problem_index]

        result = True

        number = line[0]

        for index, element in enumerate(line):
            if index == 0:
                continue
            if int(line[index]) > int(number):
                number = int(line[index])
            else:
                first_result = False
    else:
        first_result = True

    # Check the other direction
    problem_index = 0
    line = original
    number = int(line[0])

    for index, element in enumerate(line):
        if index == 0:
            continue
        if int(line[index]) < int(number):
            number = int(line[index])
        else:
            problem_index = index - 1
            result = False
            break

    if not result:
        del line[problem_index]

        result = True

        number = line[0]

        for index, element in enumerate(line):
            if index == 0:
                continue
            print(line[index], number)
            if int(line[index]) < int(number):
                number = int(line[index])
            else:
                second_result = False
    else:
        second_result = True

    if first_result or second_result:
        return True
    else:
        return False



safe_reports = 0

for index, element in enumerate(lines):
    if index != 1:
        continue
    first = checkForJump(lines[index].split())
    second = checkForConsistency(lines[index].split())

    print(first, second)

    if first and second:
        safe_reports += 1

print('-------')
print(safe_reports)
