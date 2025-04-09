inpt=open("f:\Codeing\Algorithum\week2\input2b.txt","r")
oupt=open("f:\Codeing\Algorithum\week2\output2b.txt","w")
data_into_list=inpt.readlines()
#print(data_into_list)

list1 = data_into_list[1].split()
list2 = data_into_list[3].split()
#print(list1,list2)
len_1 = len(list1)
len_2 = len(list2)
marged_lst = []
point1, point2 = 0, 0
 
while point1 < len_1 and point2 < len_2:
    if int(list1[point1]) < int(list2[point2]):
        marged_lst.append(int(list1[point1]))
        point1 += 1
 
    else:
        marged_lst.append(int(list2[point2]))
        point2 += 1
#print(marged_lst)
marged_lst = marged_lst + list1[point1:] + list2[point2:]
#print(marged_lst)
oupt.writelines(str(marged_lst))
 

