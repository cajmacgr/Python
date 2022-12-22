win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
points = {'X': 1, 'Y': 2, 'Z': 3}
score = 0
with open("Day 2\input.txt") as file:
    for line in file:
        l = line.strip()
        score += points.get(l[2])
        if l[2] != win.get(l[0]):
            if l[2] == draw.get(l[0]):
                score += 3
            else:
                score += 0
            continue
        score += 6
    print(score)