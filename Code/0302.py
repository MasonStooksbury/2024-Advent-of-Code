#!/usr/bin/python3
import copy
import re

data = ''
with open(f'../Input/03.txt', 'r') as file:
    data = file.read()

mul_regex = r"mul\(\d{1,3}\,\d{1,3}\)"

mul_positions = []
for match in re.finditer(mul_regex, data):
   mul_positions.append(match.span())

muls = re.findall(mul_regex, data)
new_muls = []
for equation in muls:
    thing = equation.split('mul')[-1]
    thing = thing[1:-1]
    left, right = thing.split(',')
    new_muls.append(int(left) * int(right))

muls_with_positions = list(zip(new_muls, [x[0] for x in mul_positions]))


do_regex = r"do\(\)"

do_positions = []
for match in re.finditer(do_regex, data):
   do_positions.append(match.span())

dos = re.findall(do_regex, data)

do_positions = [x[0] for x in do_positions]
do_positions.insert(0,0)


dont_regex = r"don\'t\(\)"

dont_positions = []
for match in re.finditer(dont_regex, data):
   dont_positions.append(match.span())

donts = re.findall(dont_regex, data)

dont_positions = [x[0] for x in dont_positions]

def findNearestDoOrDont(current_position, do_or_dont_list):
    nearest = 0
    for thing in do_or_dont_list:
        if thing < current_position:
            nearest = thing

    return int(nearest)

def doOrNah(current_position):
    nearest_do = current_position - findNearestDoOrDont(current_position, do_positions)
    nearest_dont = current_position - findNearestDoOrDont(current_position, dont_positions)

    return nearest_do <= nearest_dont


total = 0
for mul in muls_with_positions:
    if doOrNah(int(mul[1])):
        total += mul[0]

print(total)
