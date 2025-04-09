inpt=open("f:\Codeing\Algorithum\week_1\input4.txt","r")
oupt=open("f:\Codeing\Algorithum\week_1\output4.txt","w")
data_into_list=inpt.readlines()
for i in range(1,len(data_into_list)-1):
    min=data_into_list[i].split()[0]
    #print(min)
    index=i
    for j in range(i+1,len(data_into_list)):
        if min==data_into_list[j].split()[0]:
            if data_into_list[index].split()[-1]==data_into_list[j].split()[-1]:
                pass
            else:
                time_1=data_into_list[index].split()[-1].split(":")
                time_2=data_into_list[j].split()[-1].split(":")
                if time_1[0]==time_2[0]:
                    if int(time_1[1])<int(time_2[1]):
                        index=j
                else:
                    if int(time_1[0])<int(time_2[0]):
                        index=j
        if min>data_into_list[j].split()[0]:#abcd>dhumketu
            min=data_into_list[j].split()[0]
            index=j
    data_into_list[i],data_into_list[index]=data_into_list[index],data_into_list[i]

for i in range(1,len(data_into_list)):
    oupt.writelines(data_into_list[i])