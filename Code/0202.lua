#!/usr/bin/lua

input = '../Input/02.txt'

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


function checkForJump(line)
    number = line[1]
    problems = 0

    for j=2, #line do
        difference = math.abs(number - line[j])
        number = line[j]

        if difference > 3 or difference <= 0 then
            problems = problems + 1
        end
    end

    print('problems', problems)

    if problems > 1 then
        return false
    elseif problems <= 1 then
        return true
    end
end


function checkForConsistency(line)
    number = line[1]
    result = true
    first_problems = 0
    for i=2, #line do
        if tonumber(line[i]) > tonumber(number) then
            number = tonumber(line[i])
        else
            first_problems = first_problems + 1
        end
    end


    number = tonumber(line[1])
    second_problems = 0
    for i=2, #line do
        if tonumber(line[i]) < tonumber(number) then
            number = tonumber(line[i])
        else
            second_problems = second_problems + 1
        end
    end

    if first_problems <= 1 or second_problems <= 1 then
        return true
    else
        return false
    end
end



safe_reports = 0

for i=1, #lines do
    if i==3 then break end
    first = checkForJump(lines[i])
    second = checkForConsistency(lines[i])

    print(first, second)

    if first and second then
        safe_reports = safe_reports + 1
    end
end

print(safe_reports)
