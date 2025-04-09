def dfs(course, adj_list, visited, stack, rec_stack):

    #print(visited,stack,rec_stack)
    visited[course] = True
    rec_stack[course] = True

    for prereq in adj_list[course]:
        if not visited[prereq]:
            if dfs(prereq, adj_list, visited, stack, rec_stack):
                return True
        elif rec_stack[prereq]:
            return True

    rec_stack[course] = False
    #print("couse",course)

    stack.append(course)
    return False

def course_sequence_dfs(N, prerequisites):
    adj_list = {i: [] for i in range(1, N + 1)}
    for a, b in prerequisites:
        adj_list[a].append(b)

    visited = {i: False for i in range(1, N + 1)}
    stack = []
    rec_stack = {i: False for i in range(1, N + 1)}

    for course in range(1, N + 1):
        if not visited[course]:
            #print("innn",course)
            if dfs(course, adj_list, visited, stack, rec_stack):
                return "IMPOSSIBLE"

    return stack[::-1]

# Reading from file
inpt = open("f:\Codeing\Algorithum\week5\input1.txt", "r")
oupt = open("f:\Codeing\Algorithum\week5\output1a.txt", "w")
data_into_list = inpt.readlines()

N, M = map(int, data_into_list[0].split())
prerequisites = []
for line in data_into_list[1:]:
    a, b = map(int, line.split())
    prerequisites.append((a, b))

result = course_sequence_dfs(N, prerequisites)
#print(result)
if result == "IMPOSSIBLE":
    oupt.write(result)
else:
    oupt.write(' '.join(map(str, result)))

