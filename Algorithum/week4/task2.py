from collections import deque

inpt = open("f:\Codeing\Algorithum\week4\input2.txt", "r")
oupt = open("f:\Codeing\Algorithum\week4\output2.txt", "w")
data_into_list = inpt.readlines()

#print("innnnnnn",data_into_list[0].split())
N, M = map(int, data_into_list[0].split())

# Initialize an empty graph (adjacency list)
graph = {i: [] for i in range(1, N+1)}

#print(graph)



for line in data_into_list[1:]:
    u, v = map(int, line.split())
    graph[u].append(v)
    graph[v].append(u)  # Since it's bidirectional

print(graph)
#print(graph)
# BFS function
from collections import deque

def bfs(graph, start):
    visited = set() # We use set to keep the track of visited vertices
    #print(type(visited))
    queue = deque([start]) # Using Queue for BFS nad Enqueue the starting vertex
    visited.add(start) #also adding to the visited list
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(str(vertex))
# Enqueue all adjacent vertices that have not been visited
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return ' '.join(result) #to convert a list of integers (or strings)
#into a single string where each element of the list is separated by a space.


oupt.write(bfs(graph, 1))
oupt.write('\n')
