from collections import deque

inpt = open("f:\Codeing\Algorithum\week4\input3.txt", "r")
oupt = open("f:\Codeing\Algorithum\week4\output3.txt", "w")
data_into_list = inpt.readlines()

#print("innnnnnn",data_into_list[0].split())
N, M = map(int, data_into_list[0].split())

# Initialize an empty graph (adjacency list)
graph = {i: [] for i in range(1, N+1)}

for line in data_into_list[1:]:
    u, v = map(int, line.split())
    graph[u].append(v)
    graph[v].append(u)  # Since it's bidirectional

#print(graph)

from collections import deque

def dfs(graph, start):
    visited = set()

    def dfs_util(vertex):
        visited.add(vertex)
        result.append(str(vertex))

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_util(neighbor)
    result = []
    dfs_util(start)
    return ' '.join(result)

oupt.write(dfs(graph, 1))
oupt.write('\n')
