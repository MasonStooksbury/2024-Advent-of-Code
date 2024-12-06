#!/usr/bin/python3

lines = ''
with open(f'../Input/04.txt', 'r') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    new_lines.append(line[:-1])
lines = new_lines



def checkForward(rindex, lindex):
    row = lines[rindex]
    try:
        return row[lindex + 1] == 'M' and row[lindex + 2] == 'A' and row[lindex + 3] == 'S'
    except:
        return False

def checkBackward(rindex, lindex):
    row = lines[rindex]
    try:
        if lindex - 1 < 0 or lindex - 2 < 0 or lindex - 3 < 0:
            return False
        return row[lindex - 1] == 'M' and row[lindex - 2] == 'A' and row[lindex - 3] == 'S'
    except:
        return False

def checkUp(rindex, lindex):
    try:
        if rindex - 1 < 0 or rindex - 2 < 0 or rindex - 3 < 0:
            return False
        row1 = lines[rindex - 1]
        row2 = lines[rindex - 2]
        row3 = lines[rindex - 3]

        return row1[lindex] == 'M' and row2[lindex] == 'A' and row3[lindex] == 'S'
    except:
        return False

def checkDown(rindex, lindex):
    try:
        row1 = lines[rindex + 1]
        row2 = lines[rindex + 2]
        row3 = lines[rindex + 3]

        return row1[lindex] == 'M' and row2[lindex] == 'A' and row3[lindex] == 'S'
    except:
        return False

def checkNW(rindex, lindex):
    try:
        if rindex - 1 < 0 or rindex - 2 < 0 or rindex - 3 < 0 or lindex - 1 < 0 or lindex - 2 < 0 or lindex - 3 < 0:
            return False
        row1 = lines[rindex - 1]
        row2 = lines[rindex - 2]
        row3 = lines[rindex - 3]

        return row1[lindex-1] == 'M' and row2[lindex-2] == 'A' and row3[lindex-3] == 'S'
    except:
        return False

def checkNE(rindex, lindex):
    try:
        if rindex - 1 < 0 or rindex - 2 < 0 or rindex - 3 < 0:
            return False
        row1 = lines[rindex - 1]
        row2 = lines[rindex - 2]
        row3 = lines[rindex - 3]

        return row1[lindex+1] == 'M' and row2[lindex+2] == 'A' and row3[lindex+3] == 'S'
    except:
        return False

def checkSW(rindex, lindex):
    try:
        if lindex - 1 < 0 or lindex - 2 < 0 or lindex - 3 < 0:
            return False
        row1 = lines[rindex + 1]
        row2 = lines[rindex + 2]
        row3 = lines[rindex + 3]

        return row1[lindex-1] == 'M' and row2[lindex-2] == 'A' and row3[lindex-3] == 'S'
    except:
        return False

def checkSE(rindex, lindex):
    try:
        row1 = lines[rindex + 1]
        row2 = lines[rindex + 2]
        row3 = lines[rindex + 3]

        return row1[lindex+1] == 'M' and row2[lindex+2] == 'A' and row3[lindex+3] == 'S'
    except:
        return False



def checkForXmas(rindex, lindex):
    forward = checkForward(rindex, lindex)
    backward = checkBackward(rindex, lindex)
    up = checkUp(rindex, lindex)
    down = checkDown(rindex, lindex)
    nw = checkNW(rindex, lindex)
    ne = checkNE(rindex, lindex)
    sw = checkSW(rindex, lindex)
    se = checkSE(rindex, lindex)

    directions = [forward, backward, up, down, nw, ne, sw, se]

    total = 0
    for thing in directions:
        if thing:
            total += 1

    return total


total = 0
for rindex, row in enumerate(lines):
    for lindex, letter in enumerate(row):
        if letter == 'X':
            total += checkForXmas(rindex, lindex)

print(total)
