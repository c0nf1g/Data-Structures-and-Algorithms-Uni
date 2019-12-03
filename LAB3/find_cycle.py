from read_file import read_file


def dfs(v, visited, stack, graph, cycle_array):
    visited[v] = True
    stack[v] = True

    for w in graph[v]:
        if not visited[w]:
            if dfs(w, visited, stack, graph, cycle_array):
                cycle_array.append(w)
                return True
        elif stack[w]:
            cycle_array.append(w)
            return True

    stack[v] = False
    return False


def check_cycle(graph, vertics_num, v):
    visited = [False] * (len(graph) + 1)
    stack = [False] * (len(graph) + 1)
    cycle_array = []

    if not visited[v]:
        if dfs(v, visited, stack, graph, cycle_array):
            return cycle_array

    return False


def show_all_cycles(graph, vertices_num):
    for v in range(vertices_num):
        print("vertex {}     ".format(v) + check_cycle(graph, vertices_num, v).__str__() + "\n")
