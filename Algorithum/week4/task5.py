inpt = open("f:\Codeing\Algorithum\week4\input5.txt", "r")
oupt = open("f:\Codeing\Algorithum\week4\output5.txt", "w")

from collections import deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])#(1,[1])
    visited = set()

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == end:
            #print(path)
            return len(path) - 1, path

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return float('inf'), []



data_into_list = inpt.readlines()
N, M, D = map(int, data_into_list[0].split())
graph = {i: [] for i in range(1, N + 1)}
for line in data_into_list[1:]:
    u, v = map(int, line.split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)
time, path = shortest_path(graph, 1, D)
oupt.write(f"Time: {time}\n")
oupt.write(f"Shortest Path: {' '.join(map(str, path))}")
