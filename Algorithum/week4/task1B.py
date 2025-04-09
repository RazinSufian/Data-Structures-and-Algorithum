inpt=open("f:\Codeing\Algorithum\week4\input1.txt","r")
oupt=open("f:\Codeing\Algorithum\week4\output1b.txt","w")
data_into_list=inpt.readlines()


def adjacency_list_representation(N, M, edges):
    # Initialize the adjacency list with empty lists for all vertices
    adj_list = {i: [] for i in range(0, N+1)}

    for edge in edges:
        u, v, w = edge
        adj_list[u].append((v, w))
    

    for vertex, neighbors in adj_list.items():

        oupt.writelines(f"{vertex} : ")
        oupt.writelines(' '.join([f"{i}" for i in neighbors]))
        oupt.writelines("\n")


N=int(data_into_list[0].split()[0])
M = int(data_into_list[0].split()[1])

edges=[]

for i in data_into_list[1::]:
    data=i.split()
    int_value=[]
    for i in data:
        int_value.append(int(i))  
    edges.append(tuple(int_value))
adjacency_list_representation(N, M, edges)

