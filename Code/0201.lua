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
    result = true

    for j=2, #line do
        difference = math.abs(number - line[j])
        number = line[j]

        if difference > 3 or difference <= 0 then
            result = false
            break
        end
    end

    return result

    -- if result then return true end
    -- result = true
    -- print('wee')

    -- for j=2, #line do
    --     difference = math.abs(number - line[j])
    --     number = line[j]

    --     print(difference)

    --     if difference > 3 or difference <= 0 then
    --         result = false
    --         break
    --     end
    -- end

    -- return result
end


function checkForConsistency(line)
    number = line[1]
    result = true
    for i=2, #line do
        if tonumber(line[i]) > tonumber(number) then
            number = tonumber(line[i])
        else
            result = false
            break
        end
    end

    if result then return true end
    result = true
    number = tonumber(line[1])

    for i=2, #line do
        if tonumber(line[i]) < tonumber(number) then
            number = tonumber(line[i])
        else
            result = false
            break
        end
    end

    return result
end



safe_reports = 0

for i=1, #lines do
    first = checkForJump(lines[i])
    second = checkForConsistency(lines[i])

    print(first, second)

    if first and second then
        safe_reports = safe_reports + 1
    end
end

print(safe_reports)
