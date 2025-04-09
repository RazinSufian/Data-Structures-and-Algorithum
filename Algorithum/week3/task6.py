inpt=open("f:\Codeing\Algorithum\week3\input6.txt","r")
oupt=open("f:\Codeing\Algorithum\week3\output6.txt","w")
data_into_list=inpt.readlines()
data=data_into_list[1].split()
arra= [int(x) for x in data]

def partition(arr, swp_point, ite_point):
    pivot = arr[ite_point]
    swp_point = swp_point - 1
    for i in range(swp_point + 1, ite_point):
        if arr[i] < pivot:
            swp_point += 1
            arr[swp_point], arr[i] = arr[i], arr[swp_point]
    arr[swp_point + 1], arr[ite_point] = arr[ite_point], arr[swp_point + 1]
    return swp_point + 1

def quick_select(arr, start, end, k):
    if start <= end:
        par = partition(arr, start, end)
        if par == k:
            return arr[par]
        elif par < k:
            return quick_select(arr, par + 1, end, k)
        else:
            return quick_select(arr, start, par - 1, k)
    return None

#total_quaries=int(data_into_list[2].split()[0])
for i in data_into_list[3::]:
    i=int(i)     
    kth_smallest_element = quick_select(arra, 0, len(arra) - 1, i - 1)
    #print(kth_smallest_element)
    oupt.writelines(f"{kth_smallest_element}\n")

