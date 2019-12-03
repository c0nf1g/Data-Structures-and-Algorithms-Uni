def dfs(v, graph, visited, order):
    visited[v] = True

    for w in graph[v]:
        if not visited[w]:
            dfs(w, graph, visited, order)

    order.append(v)

    return order


