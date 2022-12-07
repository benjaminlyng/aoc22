import re
import copy

with open("aoc2022/day_5.txt") as f:
    raw = f.read().splitlines()
# remove empty line
raw = list(filter(lambda x: x, raw))

# Build lists of stacks
stacks = {}
for l in filter(lambda r: r[0] == "[", raw):
    for i, x in enumerate(l[1::4], start=1):
        if not stacks.get(str(i)):
            stacks[str(i)] = []
        if x != " ":
            stacks[str(i)].append(x)

stacks1 = copy.deepcopy(stacks)

moves = [l.split() for l in filter(lambda r: r[0] == "m", raw)]

for m in moves:
    n, from_, to = m[1], m[3], m[5]
    for _ in range(int(n)):
        stacks1[to].insert(0, stacks1[from_].pop(0))

# First element in each stack
top = [stacks1[str(i)][0] for i in range(1, 10)]

print("".join(top))

# part 2
stacks2 = copy.deepcopy(stacks)

for m in moves:
    n, from_, to = m[1], m[3], m[5]
    crates = [stacks2[from_].pop(0) for _ in range(int(n))]

    stacks2[to] = crates + stacks2[to]


top = [stacks2[str(i)][0] for i in range(1, 10)]

print("".join(top))
