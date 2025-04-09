inpt=open("f:\Codeing\Algorithum\week3\input4.txt","r")
oupt=open("f:\Codeing\Algorithum\week3\output4.txt","w")
data_into_list=inpt.readlines()

data=data_into_list[1].split()
arra= [int(x) for x in data]

def merge(a, b):
    list1 = a
    list2 = b
    len_1 = len(a)
    len_2 = len(b)
    merged_lst = []
    point1, point2 = 0, 0

    while point1 < len_1 and point2 < len_2:
        if list1[point1][0] < list2[point2][0]:
            merged_lst.append(list1[point1])
            point1 += 1
        else:
            merged_lst.append(list2[point2])
            point2 += 1

    merged_lst.extend(list1[point1:])
    merged_lst.extend(list2[point2:])

    return merged_lst

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


def maximize_sum(arra):

    squared_values = [(val**2, idx) for idx, val in enumerate(arra)]
    squared_values=mergeSort(squared_values) 
    i, j = 0, len(arra) - 1
    max_sum = float('-inf')
    while i < j:
        # If the index of A[j]^2 is less than or equal to i, move j to the previous position
        if squared_values[j][1] <= i:
            #print(f"j={j},lst={squared_values[j][1]}")
            j -= 1
            #print(j)
        current_sum = arra[i] + squared_values[j][0]
 
        max_sum = max(max_sum, current_sum)
        i += 1
    return max_sum

max_sum=maximize_sum(arra)

oupt.writelines(f"{max_sum}")