from more_itertools import flatten, triplewise

with open("aoc2022/day_3.txt") as f:
    lines = f.read().splitlines()
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
duplicates = []
for l in lines:
    h = int(len(l) / 2)
    a = set(l[0:h])
    b = set(l[h:])
    duplicates.append(a.intersection(b))

scores = [alphabet.index(x) + 1 for x in flatten(duplicates)]
print(sum(scores))


# Part 2
badges = []
for i, (a, b, c) in enumerate(triplewise(lines)):
    if not (i % 3 == 0):
        continue

    badges.append(set(a).intersection(set(b)).intersection(c))
scores = [alphabet.index(x) + 1 for x in flatten(badges)]
print(sum(scores))
