
inpt=open("f:\Codeing\Algorithum\week3\input5.txt","r")
oupt=open("f:\Codeing\Algorithum\week3\output5.txt","w")
data_into_list=inpt.readlines()
data=data_into_list[1].split()
arra= [int(x) for x in data]

def partition(arr,swp_point,ite_point):
    pivot=arr[ite_point]
    swp_point=swp_point-1
    for i in range(swp_point+1,ite_point):
        if arr[i]<pivot:
            swp_point+=1
            arr[swp_point],arr[i]=arr[i],arr[swp_point]
    arr[swp_point+1],arr[ite_point]=arr[ite_point],arr[swp_point+1]
    return swp_point+1

def quick_sort(arr,start,end):
    if start<end:
        par=partition(arr,start,end)
        quick_sort(arr,start,par-1)
        quick_sort(arr,par+1,end)
    return arr

quick_sorted_arra=quick_sort(arra,0,len(arra)-1)
oupt.writelines(f"{quick_sorted_arra}")
