inpt=open("f:\Codeing\Algorithum\week3\input2.txt","r")
oupt=open("f:\Codeing\Algorithum\week3\output2.txt","w")
data_into_list=inpt.readlines()
data=data_into_list[1].split()
arra= [int(x) for x in data]

def devide_conqure(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2
        a1 = devide_conqure(arr[0:mid])  
        a2 = devide_conqure(arr[mid:])  
        return max(a1,a2)


arra=devide_conqure(arra)
oupt.writelines(f"{arra}")