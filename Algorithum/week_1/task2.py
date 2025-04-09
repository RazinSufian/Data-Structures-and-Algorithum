#Task_2
inpt=open("f:\Codeing\Algorithum\week_1\input2.txt","r")
oupt=open("f:\Codeing\Algorithum\week_1\output2.txt","w")
data_into_list=inpt.readlines()
numbers=data_into_list[1].split()
#print(numbers)

for i in range(int(data_into_list[0])):
  sorted=True
  for j in range(int(data_into_list[0])-i-1):
    if int(numbers[j])>int(numbers[j+1]):
      sorted=False
      numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
  if sorted==True:
    #print(numbers)
    break

for i in numbers:
  oupt.writelines(f" {i}")
