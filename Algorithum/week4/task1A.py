import numpy as np

inpt=open("f:\Codeing\Algorithum\week4\input1.txt","r")
oupt=open("f:\Codeing\Algorithum\week4\output1.txt","w")
data_into_list=inpt.readlines()

def adjacency_matrix_representation(N, M, edges):
    matrix = np.zeros((N+1,N+1),int)
    
    for edge in edges:
        u, v, w = edge
        matrix[u][v] = w 
    for row in matrix:
        

        oupt.writelines(f"{' '.join(map(str, row))}\n")

N=int(data_into_list[0].split()[0])
M = int(data_into_list[0].split()[1])

edges=[]

for i in data_into_list[1::]:
    data=i.split()
    int_value=[]
    for i in data:
        int_value.append(int(i))  
    edges.append(tuple(int_value))
#print(edges)

adjacency_matrix_representation(N,M,edges)
