def merge(lst_1,lst_2):
    len_1=len(lst_1)
    len_2=len(lst_2)
    marged_lst=[]
    point_1,point_2=0,0
    while point_1<len_1 and point_2<len_2:
        if lst_1[point_1]<lst_2[point_2]:
            marged_lst.append(lst_1[point_1])
            point_1+=1
        else:
            marged_lst.append(lst_2[point_2])
            point_2+=1
    marged_lst= marged_lst+ lst_1[point_1:]+ lst_2[point_2:]
    return marged_lst

def merge_sort(arra):
    if len(arra)<=1:
        return arra
    else:
        mid=len(arra)//2
        a1=merge_sort(arra[:mid])
        a2=merge_sort(arra[mid:])
        return merge(a1,a2)

arra=[9,5,4,6,1,3,2,9]
print(merge_sort(arra))


#merge sort inversion count:

def merge_inversio(arra):
    def merge(lst_1,lst_2):
        len_1=len(lst_1)
        len_2=len(lst_2)
        inversion=0
        marged_lst=[]
        point_1,point_2=0,0
        while point_1<len_1 and point_2<len_2:
            if lst_1[point_1]<=lst_2[point_2]:
                marged_lst.append(lst_1[point_1])
                point_1+=1
            else:
                marged_lst.append(lst_2[point_2])
                point_2+=1
                inversion+=len_1-point_1
                print(f"Inversion= {inversion}")
        marged_lst= marged_lst+ lst_1[point_1:]+ lst_2[point_2:]
        return inversion,marged_lst

    def merge_sort(arra):
        if len(arra)<=1:
            return 0,arra
        else:
            mid=len(arra)//2
            inversion_l,a1=merge_sort(arra[:mid])
            #print(inversion_l,a1)
            inversion_r,a2=merge_sort(arra[mid:])
            inversion_t,arr=merge(a1,a2)
            inversion=inversion_l+inversion_r+inversion_t
        #print(inversion)
        return inversion,arr
    return merge_sort(arra)

inversion,array=merge_inversio(arra)
print(inversion)
    