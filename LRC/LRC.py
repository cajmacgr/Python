# Caleb MacGregor
# 2021
# LRC - A game of left, right, center

players = None
while players not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print("Please enter a number between 1 and 10")
    try:
        players = int(input("How many players are playing? : "))
        if players not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            continue
    except ValueError as e:
        pass

naming = None
names = []
while naming not in ("Y", "y", "N", "n"):
    naming = input("Would you like to use custom names? (Y/N) : ")
if naming in ("Y", "y"):
    for i in range(players):
        n = input("Enter a name: ")
        names.append(n)
if naming in ("N", "n"):
    default_names = ["Caleb", "Josiah", "Amandine", "Vincent",
                     "Fred", "Kat", "Miles", "Nala", "Sebastion", "Cooper"]  # Get new custom names
    for i in range(players):
        names.append(default_names[i])
print(names)
