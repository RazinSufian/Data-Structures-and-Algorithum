inpt= open("F:\Codeing\Algorithum\lab_final\input.txt","r")
outpt=open("F:\Codeing\Algorithum\lab_final\output.txt","w")
data_into_list=inpt.readlines()


num_checkpoints, num_roads = map(int, data_into_list[0].strip().split())


graph = []
for i in range(num_checkpoints + 1):
    graph.append([])


for line in data_into_list[1:num_roads + 1]: 
    start, end, time = map(int, line.strip().split())
    graph[start].append((end, time))

print(graph)



def dijkstra(graph, start):
    num_nodes = len(graph) - 1
    distances = [float('infinity')] * (num_nodes + 1)
    distances[start] = 0
    visited = [False] * (num_nodes + 1)

    for i in range(num_nodes):
       
        min_distance = float('infinity')
        min_node = None
        for i in range(1, num_nodes + 1):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_node = i

        if min_node is None:
            break
        
        
        visited[min_node] = True
        for neighbor, weight in graph[min_node]:
            if not visited[neighbor]:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

start_checkpoint = 1  
end_checkpoint = 7   
shortest_distances = dijkstra(graph, start_checkpoint)
shortest_time_to_university = shortest_distances[end_checkpoint]


shortest_distances_no_heapq = dijkstra(graph, start_checkpoint)
print(shortest_distances)
shortest_time_to_university_no_heapq = shortest_distances_no_heapq[end_checkpoint]


with open("F:\\Codeing\\Algorithum\\lab_final\\output.txt", "w") as outpt:
    outpt.write(str(shortest_time_to_university) + '\n')







