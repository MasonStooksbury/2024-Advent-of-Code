#!/usr/bin/python3

from pprint import pprint

lines = ''
with open(f'../Input/05.txt', 'r') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    new_lines.append(line[:-1])
lines = new_lines


rules = []
updates = []
checkpoint = False
for line in lines:
    if line == '':
        checkpoint = True
        continue
    if checkpoint:
        updates.append(line)
    else:
        rules.append(line)



# Match updates with applicable rules
update_and_rules = {}
for index, update in enumerate(updates):
    update_and_rules[index] = {'update': update, 'rules': []}
    for rule in rules:
        left, right = rule.split('|')
        if left in update and right in update:
            update_and_rules[index]['rules'].append(rule)



def isAfter(left, right, update):
    lindex = 0
    rindex = 0
    for index, page in enumerate(update.split(',')):
        if page == left:
            lindex = index
        if page == right:
            rindex = index
    return rindex > lindex


# Extract all the unique starting pages and create matches
for k,v in update_and_rules.items():
    starting_pages = []
    update_and_rules[k]['matches'] = {}
    for pages in v['rules']:
        left, right = pages.split('|')
        if left not in starting_pages:
            update_and_rules[k]['matches'][left] = [right]
            starting_pages.append(left)
        elif left in starting_pages:
            update_and_rules[k]['matches'][left].append(right)
        update_and_rules[k]['starting_pages'] = starting_pages


# pprint(update_and_rules)

good_updates = []
leave = False
for k,v in update_and_rules.items():
    good_to_go = True
    if not leave:
        for k2,v2 in v['matches'].items():
            if not leave:
                for i in v2:
                    if not leave:
                        good_to_go = isAfter(k2, i, v['update'])
                        if not good_to_go:
                            leave = True

        if good_to_go:
            good_updates.append(v['update'])
    leave = False

# print(good_updates)

total = 0
for update in good_updates:
    split = update.split(',')
    # print(int(split[(len(split)//2)]))
    total += int(split[(len(split)//2)])

print(total)
