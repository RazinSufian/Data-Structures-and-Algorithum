inpt=open("f:\Codeing\Algorithum\week2\input1a.txt","r")
oupt=open("f:\Codeing\Algorithum\week2\output1a.txt","w")
data_into_list=inpt.readlines()
target=int(data_into_list[0].split()[1])
numbers=data_into_list[1].split()
Flag=False
for i in range(len(numbers)-1):
    if Flag==True:
        break
    num_1=int(numbers[i])
    for j in range(i+1,len(numbers)):
        num_2=int(numbers[j])
        if num_1+num_2==target:
            Flag=True
            break
if Flag==False:
    oupt.writelines(f"IMPOSSIBLE")
else:
     oupt.writelines(f"{i} {j+1}")


