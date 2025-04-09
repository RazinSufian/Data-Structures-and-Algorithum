##Dummy head doubly circular link list
#dummy= the list  will contain the dummy head
#doubly= Each element will be linked to previous and next one
#circular= Last elem will be connected to dummy head

## benifit of Dummy head:

##If for intsertion or deletion if we cahnge the head of
##link list then we have to write an extra if condition for 
## retruning the list ( as return head is not goona work)
## Thats why we use dummy head, no pera in modifing the real head

import numpy as np


class Node:
  def __init__(self, e=None, n=None, p=None):
    self.element = e
    self.next = n
    self.previous = p



class DoublyList:

  # Creates a Dummy Head for Dummy Headed Circular Doubly Circular Linked List.
  def __init__(self):
    self.dummy_head=Node()
    self.count=-1



  #create a DHDCL from an array
  def create_list(self, arra):
      dh=self.dummy_head
      dh.previous=dh## Dummy_head prvious will always connect to last elem. So it will be changed
      #in each iteration
      tail=dh
      for i in range(len(arra)):
          node=Node(arra[i],dh,tail)
          tail.next=node
          tail=node
          dh.previous=node## connection dummy head previous with the lates node
      self.dummy_head=dh


  # Counts the number of Nodes in the list and return the number
  def countNode(self):
      dh=self.dummy_head
      count=0
      iteration=dh.next

      while iteration!=dh:
         count+=1
         iteration=iteration.next
      self.count=count
      return count

  # prints the elements in the list forward
  def forwardprint(self):
      dh= self.dummy_head
      iteration=dh.next
      while iteration!= dh:
        print(iteration.element, end =",")
        iteration=iteration.next
      print(" ")


  # prints the elements in the list backward
  def backwardprint(self):
      dh= self.dummy_head
      iteration=dh.previous
      while iteration!= dh:
        print(iteration.element, end =",")
        iteration=iteration.previous
      print(" ")


  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    if self.count==-1:
      self.count=self.countNode()
    if idx> self.count or idx<0:
      return None
    else:
      dh=self.dummy_head
      if idx>(self.count//2):
        iteration=dh.previous
        elem_no=self.count-1
        while elem_no!= idx:
          iteration=iteration.previous
          elem_no-=1
        return iteration
      else:
          iteration=dh.next
          elem_no=0
          while elem_no!= idx:
            iteration=iteration.next
            elem_no+=1
          return iteration

  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    dh=self.dummy_head
    iteration=dh.next
    count=0
    status=True
    while iteration!=dh:
      if iteration.element==elem:
        status=False
        return count
      iteration=iteration.next
      count+=1
    if status:
      return -1



  # insert at specific index of the DHDCL
  def insert(self, elem, idx):
    dh=self.dummy_head
    self.count=self.countNode()
    if idx> self.count or idx<0:
      return None
    else:
      if idx==self.count:
        post=dh
      else:
        post=self.nodeAt(idx)
      #print(f"indx={idx},elem={post.element}")
        prev=post.previous
        prev.next=Node(elem,post,prev)
        post.previous=prev.next


  #removes the node of the specific index and returns the element of the node
  def remove(self, idx):
    self.count=self.countNode()

    if idx> self.count or idx<0:
      return None
    else:
      node=self.nodeAt(idx)
      prev=node.previous
      post=node.next
      prev.next=post
      post.previous=prev
      node.next,node.previous=None,None
      return node.element


print("///  Test 01  ///")
h1 = DoublyList() # Creates a dummy headed doubly circular linked list
h1.create_list(np.array([10,20,30,40]))
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 10,20,30,40.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 40,30,20,10.
print('Total Nodes: ', end = ' ')
print(h1.countNode()) # This should print: 4
print()

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
print('Node at 2nd index: ', end = ' ')
n = h1.nodeAt(2)
print(n.element if n!=None else 'Index Error')# This should print: 30.
print('Node at 0th index: ', end = ' ')
n = h1.nodeAt(0)
print(n.element if n!=None else 'Index Error')# This should print: 10. IGNORE DUMMY HEAD
print('Node at -1th index: ', end = ' ')
n = h1.nodeAt(-1)
print(n.element if n!=None else 'Index Error')# This should print "index error"
print()

print("///  Test 03  ///")
print('Index of element 40:', end = ' ')
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that
print('Index of element 6:', end = ' ')
index = h1.indexOf(6)
print(index) # doesn't exists in the list this will print -1.
print()

print("///  Test 04  ///")
print('Inserting 85 in 0th index')
h1.insert(85,0)
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 85,10,20,30,40.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 40,30,20,10,85.

print()
print('Inserting 95 in 3rd index')
h1.insert(95,3)
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 85,10,20,95,30,40.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 40,30,95,20,10,85.
print()

print('Inserting 75 in 6th index')
h1.insert(75,6)
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 85,10,20,95,30,40,75.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 75,40,30,95,20,10,85.
print()


print("///  Test 05  ///")
h2 = DoublyList() # uses the constructor
h2.create_list(np.array([10, 20, 30, 40, 50, 60, 70]))
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 10,20,30,40,50,60,70.
print()

print('Removing node from 0th index')
print("Removed element: "+ str(h2.remove(0))) # This should print: Removed element: 10
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 20,30,40,50,60,70.
print('Backward Print: ', end = ' ')
h2.backwardprint() # This should print: 70,60,50,40,30,20.
print()

print('Removing node from 3rd index')
print("Removed element: "+ str(h2.remove(3))) # This should print: Removed element: 50
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 20,30,40,60,70.
print('Backward Print: ', end = ' ')
h2.backwardprint() # This should print: 70,60,40,30,20.
print()

print('Removing node from 4th index')
print("Removed element: "+ str(h2.remove(4))) # This should print: Removed element: 70
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 20,30,40,60.
print('Backward Print: ', end = ' ')
h2.backwardprint() # This should print: 60,40,30,20.
print()



