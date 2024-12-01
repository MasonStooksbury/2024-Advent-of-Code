#!/usr/bin/lua

input = '../Input/01.txt'

-- Read the file into "data"
file = {}
for line in io.lines(input) do
    file[#file + 1] = line
end

-- Split on whitespace
lines = {}
for i=1, #file do
    table.insert(lines, {})
    count = 1
    for substring in file[i]:gmatch("%S+") do
       lines[i][count] = substring
       count = count + 1
    end
end

-- Split the numbers into their own lists
first_nums = {}
second_nums = {}
for i=1, #lines do
    table.insert(first_nums, lines[i][1])
    table.insert(second_nums, lines[i][2])
end

table.sort(first_nums)

table.sort(second_nums)





local function countOccurrences(list, number)
    count = 0
    for i=1, #list do
        if list[i] == number then count = count + 1 end
    end
    return count
end


value = 0
for i=1, #first_nums do
    value = value + first_nums[i] * countOccurrences(second_nums, first_nums[i])
end

print(value)

-- value = 0
-- for i=1, #first_nums do
--     value = value + math.abs(first_nums[i] - second_nums[i])
-- end

-- print(value)
