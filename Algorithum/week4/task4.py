inpt = open("f:\Codeing\Algorithum\week4\input4.txt", "r")
oupt = open("f:\Codeing\Algorithum\week4\output4.txt", "w")
data_into_list = inpt.readlines()


N, M = map(int, data_into_list[0].split())

graph = {i: [] for i in range(1, N+1)}

for line in data_into_list[1:]:
    u, v = map(int, line.split())
    graph[u].append(v)

print(graph)


def has_cycle(graph):
    visited={i: False for i in range(1, len(graph) + 1)}
    circle_memory={i: False for i in range(1, len(graph) + 1)}
    print(visited)
    print(circle_memory)
    for vertex in range(1,len(graph) + 1):
        if not visited[vertex]:
            if circle_checker(graph, vertex, visited,circle_memory):
                return "YES"
            
    return "NO"


def circle_checker(graph,vertex,visited,circle_memory):

    visited[vertex] = True
    circle_memory[vertex] = True
    #print(f"2222-----Vertex={vertex},Visited={visited}, recursion stack={circle_memory}")
    for neighbor in graph[vertex]:#3,4
        if not visited[neighbor]:
            #print(f"parent{vertex}")
            #print(visited,circle_memory)
            if circle_checker(graph,neighbor,visited,circle_memory):
                return True
        elif circle_memory[neighbor]:
            return True
    #circle_memory={i: False for i in range(1, len(graph) + 1)}
    circle_memory[vertex] = False
    #print(f"Vertex={vertex},Visited={visited}, recursion stack={circle_memory}")
    return False
        

result = has_cycle(graph)
# print(result)
# oupt.write(result)
            
