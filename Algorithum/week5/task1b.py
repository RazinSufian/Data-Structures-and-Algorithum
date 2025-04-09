from collections import defaultdict, deque

def course_sequence_bfs(N, prerequisites):
    adj_list = defaultdict(list)
    # print(adj_list)
    in_degree = [0] * (N + 1)
    # print(in_degree)


    for a, b in prerequisites:
        adj_list[a].append(b)
        in_degree[b] += 1
 
    print(adj_list)
    print(in_degree)

    queue = deque()
    for course in range(1, N + 1):
        if in_degree[course] == 0:
            queue.append(course)

    sequence = []
    # print(queue)
    while queue:
        current_course = queue.popleft()
        sequence.append(current_course)

        for next_course in adj_list[current_course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    if len(sequence) != N:  
        return "IMPOSSIBLE"
    return sequence


inpt = open("f:\Codeing\Algorithum\week5\input1.txt", "r")
oupt = open("f:\Codeing\Algorithum\week5\output1b.txt", "w")
data_into_list = inpt.readlines()

N, M = map(int, data_into_list[0].split())
prerequisites = []
for line in data_into_list[1:]:
    a, b = map(int, line.split())
    prerequisites.append((a, b))
print(prerequisites)

result = course_sequence_bfs(N, prerequisites)
# print(result)
if result == "IMPOSSIBLE":
    oupt.write(result)
else:
    oupt.write(' '.join(map(str, result)))

