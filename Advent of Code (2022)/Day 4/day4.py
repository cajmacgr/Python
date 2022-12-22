def part1():
    with open("Day 4\input.txt") as file:
        s = 0
        for line in file:
            left = line[0:(line.find(','))]
            right = line[line.find(',')+1:line.find('\n')]
            sections = [int((left[0:left.find('-')])), int((left[left.find('-')+1:])), int((right[0:right.find('-')])), int((right[right.find('-')+1:]))]
            if (sections[0] < sections[2]) & (sections[1] >= sections[3]):
                s += 1
            elif (sections[2] < sections[0]) & (sections[3] >= sections[1]):
                s += 1
            elif sections[0] == sections[2]:
                s +=1
        return s

def part2():
    with open("Day 4\input.txt") as file:
        s = 0
        for line in file:
            left = line[0:(line.find(','))]
            right = line[line.find(',')+1:line.find('\n')]
            sections = [int((left[0:left.find('-')])), int((left[left.find('-')+1:])), int((right[0:right.find('-')])), int((right[right.find('-')+1:]))]
            if (sections[0] <= sections[2]) & (sections[1] >= sections[2]):
                s += 1
            elif (sections[2] <= sections[0]) & (sections[3] >= sections[0]):
                s += 1
        return s


print(part1())
print(part2())
