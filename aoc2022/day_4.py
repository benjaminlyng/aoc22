with open("day_4.txt") as f:
   groups = f.read().replace('-', ',').splitlines()
groups = list(map(lambda x: list(map(int,x.split(','))), groups))

print(sum(((a <= c) and (b >= d)) or ((a>=c) and (b<=d)) for a,b,c,d in groups))
# part 2
print(sum(not ((a > d) or (b < c)) for a,b,c,d in groups))
