inpt=open("f:\Codeing\Algorithum\week2\input3.txt","r")
oupt=open("f:\Codeing\Algorithum\week2\output3.txt","w")
data_into_list=inpt.readlines()

def merge(lst_1,lst_2):
    #print(lst_1,lst_2)
    len_1=len(lst_1)
    len_2=len(lst_2)
    marged_lst=[]
    point_1,point_2=0,0
    while point_1<len_1 and point_2<len_2:
        #print(lst_1[point_1].split()[1],lst_2[point_2].split()[1])
        if int(lst_1[point_1].split()[1])<int(lst_2[point_2].split()[1]):
            marged_lst.append(lst_1[point_1])
            point_1+=1
        else:
            marged_lst.append(lst_2[point_2])
            point_2+=1  
    marged_lst= marged_lst+ lst_1[point_1:]+ lst_2[point_2:]
    #print("marged",marged_lst)
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
answer=[]
count=0
last_one_end_time=0
for j in sorted:
    present_one_start_time=int(j.split()[0])
    if present_one_start_time>=last_one_end_time:
        count+=1
        answer.append(j)
        last_one_end_time=int(j.split()[1])

oupt.writelines(f"{count}\n")
for i in answer:
    oupt.writelines(i)
    
        


