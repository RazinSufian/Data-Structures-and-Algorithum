inpt=open("f:\Codeing\Algorithum\week_1\input1a.txt","r")
oupt=open("f:\Codeing\Algorithum\week_1\output1a.txt","w")
data_into_list=inpt.readlines()
print (data_into_list)
count=1
for i in range(int(data_into_list[0])):
  if int(data_into_list[count])%2==0:
    oupt.writelines(f"{data_into_list[count].strip()} is an Even number.\n")
  else:
    oupt.writelines(f"{data_into_list[count].strip()} is an odd number.\n")
  count+=1