win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
points = {'X': 1, 'Y': 2, 'Z': 3}
score = 0
with open("Day 2\input.txt") as file:
    for line in file:
        l = line.strip()
        if l[2] == "X": #Need to lose
            score += points.get(lose.get(l[0]))
        elif l[2] == "Y": #Need to draw
            score += points.get(draw.get(l[0])) + 3
        else: #Need to win
            score += points.get(win.get(l[0])) + 6
print(score)