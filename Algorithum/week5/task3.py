from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def dfs(graph, u, visited, stack):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited, stack)
    stack.append(u)

def transpose_graph(graph):
    transposed = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def dfs_scc(graph, u, visited, component):
    visited[u] = True
    component.append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs_scc(graph, v, visited, component)

def find_scc(graph, n):
    visited = {u: False for u in range(1, n + 1)}
    stack = []
    for u in graph:
        if not visited[u]:
            dfs(graph, u, visited, stack)

    transposed = transpose_graph(graph)
    visited = {u: False for u in range(1, n + 1)}
    strongly_connected_components = []

    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs_scc(transposed, u, visited, component)
            strongly_connected_components.append(component)

    return strongly_connected_components


inpt = open("f:\Codeing\Algorithum\week5\input3.txt", "r")
oupt = open("f:\Codeing\Algorithum\week5\output3.txt", "w")
data_into_list = inpt.readlines()

N, M = map(int, data_into_list[0].split())

graph = defaultdict(list)
for i in range(1, M + 1):
    u, v = map(int, data_into_list[i].split())
    add_edge(graph, u, v)

visited = {u: False for u in range(1, N + 1)}
for u in range(1, N + 1):
    if not visited[u]:
        add_edge(graph, u, u)  # Add self-loop for disconnected components
        dfs(graph, u, visited, [])

scc = find_scc(graph, N)
#print(scc)

# Writing output to file
for component in scc:
    oupt.write(' '.join(map(str, component)) + '\n')

