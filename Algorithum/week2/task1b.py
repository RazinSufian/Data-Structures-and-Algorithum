inpt=open("f:\Codeing\Algorithum\week2\input1a.txt","r")
oupt=open("f:\Codeing\Algorithum\week2\output1a.txt","w")
data_into_list=inpt.readlines()
target=int(data_into_list[0].split()[1])
numbers=data_into_list[1].split()
p1=0
p2=len(numbers)-1
flag=True
while flag==True:
    if p1>=p2:
        break
    sum=int(numbers[p1])+(int(numbers[p2]))
    if sum==target:
        flag=False
    elif sum< target:
        p1+=1
    else:
        p2-=1

if flag==True:
    oupt.writelines(f"IMPOSSIBLE")
else:
     oupt.writelines(f"{p1+1} {p2+1}")




