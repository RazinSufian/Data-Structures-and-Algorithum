#hash_table:

class Node:
  def __init__(self,key,value):
      self.key=key
      self.value=value
      self.next=None

def hash_index_creator(data,len_of_hashARRA):
    value=0
    step=1
    for i in data:
        if step==1:
            if i ==type(str):
                value+=ord(i)
            else:
                value+=i
            step+=1
        else:
            if i ==type(str):
                value-=ord(i)
            else:
                value-=i
            step-=1
    value=abs(value)%len_of_hashARRA
    return value
#key=name
#value=Mobile_number
def data_entry(hash_table,key,value):
    indx=hash_index_creator(value)
    node=Node(key,value)
    if hash_table[indx]!=0:
        hash_table[indx]=node
    else:
        tail= hash_table[indx]
        while tail.next != None:
            tail=tail.next
        tail.next=node
       