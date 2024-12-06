#!/usr/bin/python3

lines = ''
with open(f'../Input/04.txt', 'r') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    new_lines.append(line[:-1])
lines = new_lines


def checkForMs(rindex, lindex):
    if rindex - 1 < 0 or lindex - 1 < 0:
        return False
    try:
        left = (lines[rindex-1][lindex-1] == 'M' and lines[rindex+1][lindex-1] == 'M')
        right = (lines[rindex-1][lindex+1] == 'M' and lines[rindex+1][lindex+1] == 'M')
        up = (lines[rindex-1][lindex-1] == 'M' and lines[rindex-1][lindex+1] == 'M')
        down = (lines[rindex+1][lindex-1] == 'M' and lines[rindex+1][lindex+1] == 'M')
        return any([left, right, up, down])
    except:
        return False

def checkForSs(rindex, lindex):
    if rindex - 1 < 0 or lindex - 1 < 0:
        return False
    try:
        left = (lines[rindex-1][lindex-1] == 'S' and lines[rindex+1][lindex-1] == 'S')
        right = (lines[rindex-1][lindex+1] == 'S' and lines[rindex+1][lindex+1] == 'S')
        up = (lines[rindex-1][lindex-1] == 'S' and lines[rindex-1][lindex+1] == 'S')
        down = (lines[rindex+1][lindex-1] == 'S' and lines[rindex+1][lindex+1] == 'S')
        return any([left, right, up, down])
    except:
        return False


def checkForXmas(rindex, lindex):
    ms = checkForMs(rindex, lindex)
    ss = checkForSs(rindex, lindex)

    return ms and ss


total = 0
for rindex, row in enumerate(lines):
    for lindex, letter in enumerate(row):
        if letter == 'A':
            total += checkForXmas(rindex, lindex)

print(total)
