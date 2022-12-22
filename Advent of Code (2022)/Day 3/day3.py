priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32,
 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 
 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

def part1():
    s = 0
    with open("Day 3\input.txt") as file:
        for line in file:
            left = line[0:(len(line)//2)]
            right = line[(len(line)//2):]
            difference = list(set(list(left)).intersection(set(list(right))))
            s += priorities.get(difference[0])
    print(s)

def comparison(compare):
    difference1 = list(set(compare[0]).intersection(set(compare[1])))
    difference2 = list(set(difference1).intersection(set(compare[2])))
    return priorities.get(difference2[0])
    

def part2():
    s = 0
    index = 0
    with open("Day 3\input.txt") as file:
        lines = file.readlines()
        while(index < len(lines)):
            triple = []
            for _ in range(3):
                triple.append(lines[index].strip())
                index += 1
            s += comparison(triple)
    print(s)

part1()
part2()