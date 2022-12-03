with open("aoc2022/day_1.txt") as f:
    lines = f.read().splitlines()
groups = []
current = []
for l in lines:
    if l:
        current.append(int(l))
    else:
        groups.append(current)
        current = []

print(max(map(sum, groups)))

# Part 2
print(sum(sorted(map(sum, groups), reverse=True)[0:3]))
