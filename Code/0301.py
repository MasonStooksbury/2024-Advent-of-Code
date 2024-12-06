#!/usr/bin/python3
import copy
import re

data = ''
with open(f'../Input/03.txt', 'r') as file:
    data = file.read()


muls = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", data)

total = 0
for equation in muls:
    thing = equation.split('mul')[-1]
    thing = thing[1:-1]
    left, right = thing.split(',')
    total += int(left) * int(right)

print(total)
