with open("Day 1\input.txt") as file:
    calories = []
    s = 0
    for line in file:
        if line == "\n":
            calories.append(s)
            s = 0
            continue
        s = s + int(line.strip())
    top_3 = 0
    for _ in range(3):
        top_3 += max(calories)
        calories.remove(max(calories))
    print(top_3)