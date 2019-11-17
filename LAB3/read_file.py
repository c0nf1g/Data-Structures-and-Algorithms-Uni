from collections import defaultdict


def read_file(name):
    graph = defaultdict(list)

    with open(name, "r") as file:
        vertex_num = file.readline()

        for line in file:
            if " " in line:
                edge = line.split(" ")
                graph[int(edge[0])].append(int(edge[1]))

    sorted(graph[4])

    return graph, int(vertex_num)
