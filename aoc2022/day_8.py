from operator import itemgetter

with open("aoc2022/day_8.txt") as f:
    trees = f.read().splitlines()

l = len(trees)
b = len(trees[0])

fliped = [list(map(itemgetter(i), trees)) for i in range(l)]


visible = set()
# Left to right
for y, row in enumerate(trees):
    top = "-1"
    for x, height in enumerate(row):
        if height > top:
            visible.add(str(x) + "," + str(y))
            top = height

# right to left
for y, row in enumerate(trees):
    top = "-1"
    for x, height in enumerate(row[::-1]):
        if height > top:
            visible.add(str(l - 1 - x) + "," + str(y))
            top = height


# top to bottom
for x, row in enumerate(fliped):
    top = "-1"
    for y, height in enumerate(row):
        if height > top:
            visible.add(str(x) + "," + str(y))
            top = height
# bottom up
for x, row in enumerate(fliped):
    top = "-1"
    for y, height in enumerate(row[::-1]):
        if height > top:
            visible.add(str(x) + "," + str(l - 1 - y))
            top = height

print(len(visible))
