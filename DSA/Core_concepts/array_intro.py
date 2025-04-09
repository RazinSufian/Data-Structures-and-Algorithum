import numpy as np

def iteration (source):
    for i in range (len(source)):
      print(source[i])

def reverse_iteration (source):
    for i in range (len(source)-1,-1,-1):
      print(source[i])

import numpy as np
def resizeArray( oldArray, newCapacity):
    newarray=np.ones(newCapacity)
    for i in range (len(newarray)):
      newarray[i]=oldArray[i]
    return newarray

#reversing
#craating a brand new reversed array is less effcient(out_of_place_reverse)
#swapping is the best efficent approch(in_place_reverse)
def reverse_Array_out_of_the_place(arr):
    i=0
    j=len(arr)-1
    rev_arr=np.ones(len(arr), int)
    while i<len(arr):#not i<j
      rev_arr[i]=arr[j]
      i+=1
      j-=1
    return rev_arr

def reverse_Array_in_the_place(arr):
    i=0
    j=len(arr)-1
    while i<j:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j-=1
    return arr


#shifting an array left:
#ex:[5, 3, 9, 13, 2]>>[3, 9, 13, 2, None ]
#shifting an array right:
#ex:[5, 3, 9, 13, 2]>>[None, 5, 3, 9, 13]
#rotaing an array left:
#ex:[5, 3, 9, 13, 2]>>[3, 9, 13, 2, 5]
#rotaing an array right:
#ex:[5, 3, 9, 13, 2]>>[2, 5, 3, 9, 13]

def shiftlest(arr):
    for i in range (1, len(arr)):
      arr[i-1]=arr[i]
      arr[len(arr)-1]=None
      return arr

def shiftRight(arr):
    for i in range (len(arr)-1,0,-1):
      arr[i]=arr[i-1]
    arr[0]=None
    return arr

def rotate_left(arr):
    temp=arr[0]
    for i in range (1, len(arr)):
      arr[i-1]=arr[i]
      arr[len(arr)-1]=temp
      return arr
def rotate_right(arr):
    temp=arr[len(arr)-1]
    for i in range (len(arr)-1,0,-1):
      arr[i]=arr[i-1]
      arr[0]=temp
      return arr
  
def insert_element(arr,size,elem,index):
    if size==len(arr):
      print("No_space_left")
    else:
      for i in range (size, index, -1):
        arr[i]= arr[i-1]
      arr[index]=elem
      return arr
  
def remove_element(arr,index,size):
    for i in range (index +1, size):
      arr[i-1]=arr[i]
    arr[size-1]=None
    return arr
