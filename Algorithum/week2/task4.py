import numpy as np
inpt=open("f:\Codeing\Algorithum\week2\input4.txt","r")
oupt=open("f:\Codeing\Algorithum\week2\output4.txt","w")
data_into_list=inpt.readlines()
def merge(lst_1,lst_2):
    len_1=len(lst_1)
    len_2=len(lst_2)
    marged_lst=[]
    point_1,point_2=0,0
    while point_1<len_1 and point_2<len_2:
        if int(lst_1[point_1].split()[1])<int(lst_2[point_2].split()[1]):
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
sorted=merge_sort(data_into_list[1::])
print(sorted)
pointer=0
#print(data_into_list[0].split()[1])
workers=int(data_into_list[0].split()[1])
arra=np.zeros(workers,int)
count=0
for i in sorted:
    if int(i.split()[0])>=arra[pointer]:
        #print(f"i={i},pointer={pointer},arra_pointer={arra[pointer]}")
        arra[pointer]=int(i.split()[1])
        count+=1
        pointer=(pointer+1)%(int(data_into_list[0].split()[1]))
oupt.writelines(str(count))
