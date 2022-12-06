with open("aoc2022/day_6.txt") as f:
    raw = f.read()
for i, _ in enumerate(raw):
    if len(set(raw[i : i + 4])) == 4:
        print(i + 4)
        break
# Part 2
for i, _ in enumerate(raw):
    if len(set(raw[i : i + 14])) == 14:
        print(i + 14)
        break
