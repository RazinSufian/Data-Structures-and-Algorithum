inpt=open("f:\Codeing\Algorithum\week3\input1.txt","r")
oupt=open("f:\Codeing\Algorithum\week3\output1.txt","w")
data_into_list=inpt.readlines()
data=data_into_list[1].split()
arra= [int(x) for x in data]

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
    
arra=merge_sort(arra)
oupt.writelines(f"{arra}")
