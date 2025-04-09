inpt=open("f:\Codeing\Algorithum\week_1\input1b.txt","r")
oupt=open("f:\Codeing\Algorithum\week_1\output1b.txt","w")
data_into_list=inpt.readlines()
def caluculation(a,b,sign):
  if sign=="-":
    return a-b
  elif sign=="+":
    return a+b
  elif sign=="*":
    return a*b
  else:
    return a/b

count=1
for i in range(int(data_into_list[0])):
  lst=data_into_list[count].split()
  ans=caluculation(int(lst[1]),int(lst[3]),lst[2])
  oupt.writelines(f"The result of {lst[1]} {lst[2]} {lst[3]} is {ans}.\n")
  count+=1