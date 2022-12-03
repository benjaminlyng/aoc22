with open("aoc2022/day_2.txt") as f:
    lines = f.read().splitlines()
scores = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}
rounds = list(map(lambda x: x.split(), lines))
results = [scores[a][b] for a, b in rounds]
choices = [["X", "Y", "Z"].index(choice) + 1 for _, choice in rounds]
print(sum(results) + sum(choices))

# Part 2
scores_2 = {
    "A": {"X": 0 + 3, "Y": 3 + 1, "Z": 6 + 2},
    "B": {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3},
    "C": {"X": 0 + 2, "Y": 3 + 3, "Z": 6 + 1},
}
results = [scores_2[a][b] for a, b in rounds]
print(sum(results))
