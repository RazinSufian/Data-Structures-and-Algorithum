from task1 import merge_sort
inpt=open("f:\Codeing\Algorithum\week3\input3.txt","r")
oupt=open("f:\Codeing\Algorithum\week3\output3.txt","w")
data_into_list=inpt.readlines()
data=data_into_list[1].split()
arra=[]
for i in data:
    arra.append(int(i))
sorted_arra=merge_sort(arra)
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
count=0
length=len(sorted_arra)
for i in arra:
    indx=binary_search(sorted_arra,i)
    count+=indx
    sorted_arra.pop(indx)
oupt.writelines(f"{count}")


