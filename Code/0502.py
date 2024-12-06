#!/usr/bin/python3

from pprint import pprint
from collections import OrderedDict

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

good_updates = {}
leave = False
lazy_count = 0
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
                            good_updates[lazy_count] = {}
                            good_updates[lazy_count]['update'] = v['update']
                            good_updates[lazy_count]['matches'] = v['matches']
                            lazy_count += 1

    leave = False

# pprint(good_updates)

# All of them look like this. If we sort them by array length, all we have to do is start
#   from the smallest one and work backwards 13->29->47->75->97 = 97,75,47,29,13
# 2: {'matches': {'29': ['13'],
#                 '47': ['13', '29'],
#                 '75': ['29', '47', '13'],
#                 '97': ['13', '47', '29', '75']},
#     'update': '97,13,75,29,47'}}

new_dict = {}
count = 0
total = 0
for k,v in good_updates.items():
    sorted_dict = OrderedDict(sorted(v['matches'].items(), key = lambda x : len(x[1]))).items()
    # new_dict[count] = {}
    # new_dict[count]['update'] = v['update']
    # new_dict[count]['matches'] = sorted_dict
    # count += 1

    # print(sorted_dict)
    new_order = []
    count = 0
    for k2,v2 in sorted_dict:
        if count == 0:
            new_order.append(v2[0])
        new_order.append(k2)
        count += 1
    total += int(new_order[(len(new_order)//2)])

print(total)
