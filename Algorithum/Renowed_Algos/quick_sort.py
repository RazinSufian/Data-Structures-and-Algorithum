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

arra=[2,4,9,5,8,1,7,6]
print(quick_sort(arra,0,len(arra)-1))
