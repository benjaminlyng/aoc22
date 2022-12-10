# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
import redis
from more_itertools import one
from operator import itemgetter

with open("aoc2022/day_10.txt") as f:
    cmds = f.read().splitlines()
# Initialize Redis timeseries
r = redis.Redis(host="localhost", port=6379, db=0)
ts = r.ts()
r.delete("x")
r.set("t", 1)
ts.add("x", 0, 1)
# Run commands
for cmd in cmds:
    # Increase clock counter
    r.incr("t")
    if cmd == "noop":
        continue

    r.incr("t")
    _, value = cmd.split()
    clock = int(r.get("t"))
    # store value in redis timeseris using clock-time as timestamp
    ts.incrby("x", int(value), clock)


def get_value_at_clock(ts, t):
    res = ts.revrange("x", 0, t, count=1)
    return one(res)[1]


cycles = [20]
cycles.extend(range(60, clock, 40))
signals = [get_value_at_clock(ts, i) * i for i in cycles]
print(sum(signals))  # 13740

# Part 2
output = []
for i in range(clock + 1):
    v = get_value_at_clock(ts, i + 1)
    j = i % 40
    if v <= j + 1 and v >= j - 1:
        output.append("#")
    else:
        output.append(".")

for i in range(6):
    print("".join(output[i * 40 : i * 40 + 40]))

# ####.#..#.###..###..####.####..##..#....
# ...#.#..#.#..#.#..#.#....#....#..#.#....
# ..#..#..#.#..#.#..#.###..###..#....#....
# .#...#..#.###..###..#....#....#....#....
# #....#..#.#....#.#..#....#....#..#.#....
# ####..##..#....#..#.#....####..##..####.
