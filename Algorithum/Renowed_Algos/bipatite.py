from collections import deque

inpt = open("f:\Codeing\Algorithum\week4\input2.txt", "r")
oupt = open("f:\Codeing\Algorithum\week4\output2.txt", "w")
data_into_list = inpt.readlines()

N, M = map(int, data_into_list[0].split())

graph = {i: [] for i in range(0, N+1)}


for line in data_into_list[1:]:
    u, v = map(int, line.split())
    graph[u].append(v)
print(graph)
from collections import deque

def Bipartite_bfs(graph, start):
    queue    = deque() 
    queue.append((start,"blue"))
    visited= {}
    while queue:
        print(queue)
        vertex = queue.popleft()
        visited[vertex[0]]=vertex[1]

        if vertex[1]=="blue":color="red"
        else:color="blue"

        for neighbor in graph[vertex[0]]:
            if neighbor not in visited.keys():
                if any( number == neighbor and col!= color  for number, col in queue):
                    return (visited,False)
                queue.append((neighbor,color))




    return visited,True


a,b=Bipartite_bfs(graph, 0)
print(a)
print(b)


#Bipartite_dfs:
def Bipartite_dfs(graph, start, color, visited):
    visited[start] = color
    
    next_color = "blue" if color == "red" else "red"
    
    for neighbor in graph[start]:
        if neighbor in visited:
            if visited[neighbor] == visited[start]:
                print(neighbor)
                print("innnn")
                return (False)
        else:
            if not Bipartite_dfs(graph, neighbor, next_color, visited):
                return (visited, False)
    
    return visited, True

def BipartiteDFS(graph):
    visited = {}
    for vertex in graph:
        if vertex not in visited:
            if not Bipartite_dfs(graph, vertex, "blue", visited):
                return visited, False
    
    return visited, True

# Example usage:
# Assuming 'graph' is defined similarly as in the previous code snippets

a, b = BipartiteDFS(graph)
print(a)
print(b)

