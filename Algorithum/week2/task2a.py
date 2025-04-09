inpt=open("f:\Codeing\Algorithum\week2\input2b.txt","r")
oupt=open("f:\Codeing\Algorithum\week2\output2a.txt","w")
data_into_list=inpt.readlines()
list1 = data_into_list[1].split()
list2 = data_into_list[3].split()
new_list=list1+list2

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
    
    
sorted=merge_sort(new_list)


oupt.writelines(str(sorted))
 

