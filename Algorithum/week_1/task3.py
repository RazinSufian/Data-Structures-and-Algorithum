#Task_3
inpt=open("f:\Codeing\Algorithum\week_1\input3.txt","r")
oupt=open("f:\Codeing\Algorithum\week_1\output3.txt","w")
data_into_list=inpt.readlines()
rolls=data_into_list[1].split()
marks=data_into_list[2].split()

def ID_Num_seq_selection_srt(arr,arr_2):
    for i in range(0,len(arr)-1):
        max=arr[i]
        index=i
        for j in range(i+1,len(arr)):
            if max==arr[j]:
                if arr_2[index]>arr_2[j]:
                    max=arr[j]
                    index=j
            if max<arr[j]:
                max=arr[j]
                index=j
        arr[i],arr[index]=arr[index],arr[i]
        arr_2[i],arr_2[index]=arr_2[index],arr_2[i]
    return arr,arr_2
sorted_marks,modified_rools=ID_Num_seq_selection_srt(marks,rolls)
for i in range(len(sorted_marks)):
    oupt.writelines(f"ID: {modified_rools[i]} Mark: {sorted_marks[i]}\n")