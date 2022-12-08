# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
import redis
from redis.commands.graph import Node
from more_itertools import pairwise

r = redis.Redis(host="localhost", port=6379, db=0)
graph = r.graph(index_name="day_7")


def create_file_path(graph, path, file, size):
    q = ""
    for i, dir in enumerate(path):
        q += f"""Merge (o{i}:dir {{name:'{"/".join(path[0:i+1])}'}}) """
    j = 0
    for i, j in pairwise(range(len(path))):
        q += f"""Merge (o{i}) - [:contains] -> (o{j}) """

    q += f"MERGE (o{j}) - [:contains] -> (f:file {{name: '{file}', size: {size}}})"
    graph.query(q)


def populate_graph(graph):
    try:
        graph.delete()
    except:
        pass

    with open("aoc2022/day_7.txt") as f:
        raw = f.read().splitlines()

    path = []
    for out in raw:
        if out in ("$ ls"):
            continue
        elif out == "$ cd ..":
            path.pop()
        elif out[0:4] == "$ cd":
            path.append(out[5:])
        elif out[0:3] == "dir":
            continue
        else:
            size, filename = out.split()
            create_file_path(graph, path, filename, int(size))


populate_graph(graph=graph)
q = """
    MATCH (n:dir) - [*] -> (o:file) 
    WITH n, sum(o.size) as s 
    WHERE s < 100000  with s 
    RETURN sum(s)
    """
print(graph.query(q).result_set)  # 1077191

# part 2
q = """
    MATCH (n:dir {name:'/'}) - [*] -> (o:file) 
    WITH n, sum(o.size) as s 
    WITH 30000000 - 70000000 + sum(s) as t
    MATCH (n:dir) - [*] -> (o:file) 
    WITH n, sum(o.size) as s, t 
    WHERE s > t  with n, s
    RETURN min(s)
    """
print(graph.query(q).result_set)  # 5649896
