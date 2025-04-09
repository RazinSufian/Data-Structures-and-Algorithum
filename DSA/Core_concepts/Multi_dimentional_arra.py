import numpy as np

import numpy as np
arra=np.zeros((8,2),int)
# This means we are creating 8 arrays in a single colom. Each arrays contain 2 elemnts.
#so, colom number will represent how many elemnts are in array
#The arra would be like:-
#     [[0 0]
#      [0 0]
#      [5 0]
#      [0 0]
#      [0 0]
#      [0 0]
#      [0 0]
#      [0 0]]
# Their indexing would be 
#1st row [0,0],[0,1]
#2nd row [1,0],[1,1]
#3nd row [2,0],[2,1]
#4th row [3,0],[3,1]
#5nd row [4,0],[4,1]..... And so on

#But remember if we run a single loop in a arra. Like For i in arra:
# I will give us 8 outputs not 16

#Conclusion:There are total 8 elemts, But total number of indexing places are 16....


#creating_dimentional_array:
arra_1=np.array([2,4,6,8,10,12]).reshape(2,3)
m=np.zeros((2,3), dtype=int)
# Rember RC, First one represents= row ; the second one represents = colom
n=np.array([[4,3,8],[2,5,2]])
print("yasinnn")
row, colom = arra.shape[0]
#shape returns a tuple, which contains row and colom of an arra
# Creat an empry dimentional_array:
def creat_array():
    dimentioal_array=np.zeros((2,3), dtype=int)
    for i in range (2):
        for j in range (3):
            print(f"Enter element of:[{i}][{j}]")
            dimentioal_array[i][j]=int(input())
    return dimentioal_array

def creat_array():
    dimentioal_array=np.zeros((2,3), dtype=int)
    num=2
    for i in range (2):
        for j in range (3):
                dimentioal_array[i][j]=num
                num+=2
    return dimentioal_array
    
arra_2= creat_array()

print(arra_2)
def row_iterartion(arr):
    row,colom=arr.shape
    for i in range (row):
        for j in range (colom):
            print(arr[i][j], end=" ")
        print()

row_iterartion(arra_2)

def colom_iterartion(arr):
    row,colom=arr.shape

    for i in range(colom):
        for j in range(row):
            print(arr[j][i], end=" ")
        print()

colom_iterartion(arra_2)

def sum_of_every_row(arr):
    row,colom=arr.shape
    answer_arr=np.zeros((row,1),int)
    for i in range(row):
        row_sum=0
        for j in range(colom):
            row_sum+= arr[i][j]
        answer_arr[i][0]=row_sum
    return answer_arr

sum_of_every_row(arra_2)

arra_1=np.array([1,2,3,4,5,6]).reshape(2,3)
arra_2=np.array([1,2,3,4,5,6]).reshape(3,2)


def array_maltipiacation(arra_1, arra_2):
    R_1,C_1=arra_1.shape
    R_2,C_2=arra_2.shape
    if C_1 != R_2:
        return False
    else:
        ans_arr=np.zeros((R_1,C_2),int)
        for i in range(R_1):
            for j in range (C_2):
                multi=0
                for k in range (R_2):
                  ans_arr[i][j]+=arra_1[i][k]*arra_2[k][j]
                  #or
                  #multi+=arra_1[i][k]*arra_2[k][j]
                #ans_arr[i][j]=multi
        return ans_arr

print(array_maltipiacation(arra_1,arra_2))



