from collections import defaultdict


def read_file(name):
    graph = defaultdict(list)

    with open(name, "r") as file:
        for line in file:
            edge = line.split(" ")
            graph[edge[0].strip()].append(edge[1].strip())
    with open(name, "r") as file:
        for line in file:
            edge = line.split(" ")
            if edge[1].strip() not in graph:
                graph[edge[1].strip()].append([])
                graph[edge[1].strip()].remove([])

    return graph

