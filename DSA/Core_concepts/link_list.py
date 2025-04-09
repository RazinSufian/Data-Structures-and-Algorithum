import numpy  as np

class Node:
  def __init__(self,data,nxt=None):
    self.elem=data
    self.next=nxt
    #self.previous=None

#convert and arra to a Link_list and return head:
    
def createList(arr):
  head=Node(arr[0])
  tail=head
  for i in range(1,len(arr)):
    new_node=Node(arr[i])
    tail.next=new_node #Linking_it_with_the_previous_element
    tail=new_node #making_it_the_new_tail,
    #Note: New_node.next a by defult None set hocche; we are not modifing it, in this step
  return head

#print a link list, parameter (Head)

def printLinkedList(head):
  temp = head
  while temp != None:# This condition will stop the link_list in the last element, becausu temp = temp.next
    if temp.next != None:# this cond. will print all the elem of link list except hte last one, to solve the "end=" problem
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)# This will print the last elem of link list
    temp = temp.next
  print()

#length of a link_list

def Node_len(head):
  count=0
  temp=head
  while temp!= None: # if we use temp.next!= none, then initial counter would be 1. becuse the loop will only run untill the 2nd last element
    count+=1
    temp=temp.next
  return count

#giving an index_ return (the elem address) of that index


def NodeAt(head,index):
  count=0
  temp=head
  obj=None
  while temp!= None:
    if count==index:
      obj=temp
      break
    temp=temp.next
    count+=1
  print("Invalid_index")
  return (obj)


def Node_del(head,index):
  if index==0:
    temp=head
    head=head.next #or temp.next
    temp.next=None #"for safety"
    return head
  elif index>0 and index<Node_len(head):
    del_previous=NodeAt(head,index-1)
    del_elem=del_previous.next
    del_next=del_elem.next
    del_previous.next=del_next
    del_elem.next=None
    return head
  else:
    return"Invalid_index"
  

def Node_inser(head,elem,index=None):
  new_node=Node(elem)
  if index==None or index==0:
    temp=head
    head=new_node
    new_node.next(temp)
    return head
  elif 0<index<Node_len(head):
    prev_node=NodeAt(head,index-1)
    next_node=prev_node.next
    prev_node.next=new_node
    new_node.next=next_node
    return head
  else:
    return"Invalid_index"
  
def Link_list_in_place_reverse(head): # Note this will change the actual link list
  prev_ind_of_temp_head=head
  temp_head=head.next #we are going to remove the head.next
  # So,before removing it we are saving it for moving to the next element
  head.next=None# as head going to be tail now
  while temp_head!= None:
    address_store_for_iteration=temp_head.next #as we are going to change the 
    #temp_head.next and connect it with the reverse element, befor changing it
    # we have to store it, to move to the next element
    temp_head.next=prev_ind_of_temp_head # temp_head.next will be connect with the 
    #very last reverse element (which is actually the previous elment of temp_head)
    prev_ind_of_temp_head=temp_head #prev_ind_of_temp_head it will always store the 
    #very last iterationn elemnet address
    #like when temp_head is 41, it will be 34
    temp_head=address_store_for_iteration # moving  to the next elementr
    
  return (prev_ind_of_temp_head)



###Againg doing it short:

def Link_list_in_place_reverse(head):
  new_head=None
  temp=head

  while temp!= None:

    address_store_for_iteration=temp.next 
    temp.next=new_head
    new_head=temp
    temp=address_store_for_iteration 

  return (new_head)
















def Link_list_out_place_reverse(head):

  temp=head
  new_head=None
  while temp!=None:
    node=Node(temp.elem,new_head)
    new_head=node
    temp=temp.next
  return new_head








head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
#print(head.next.next.elem)
printLinkedList(Link_list_out_place_reverse(head))



# a=NodeAt(head,3)
# print(a.elem)
# printLinkedList(Node_del(head,0))
# #printLinkedList(Node_inser(head,89,4))







