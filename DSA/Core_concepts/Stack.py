import numpy as np
class Node:
    def __init__(self,data):
        self.element=data
        self.next=None

#link list based implimantation
class Stack_link_list: 
    def __init__(self):
        self.Top=None
    
    def push(self,elem):
        if self.Top==None:
            self.Top=Node(elem)
        else:
            new_node=Node(elem)
            new_node.next=self.Top
            self.Top=new_node

    def pop(self):
        if self.Top==None:
            return None
        else:
            popped=self.top
            self.Top=self.top.next
            popped.next=None
        return popped.element
    
    def peek(self):
        if self.Top==None:
            return None
        else:
            return self.Top.element
    def print_stack(self):
        iterate=self.Top
        while iterate.next!= None:
            print(iterate.element)
            iterate=iterate.next

##array based implimentation
class Stack_arra:
    def __init__(self,len):
        self.array=np.zeros(len)
        self.top=-1
        self.len=len
    def push(self,data):
        if self.top+1>=self.len:
            return "Over Flow"
        self.top+=1
        self.array[self.top]=data
    def peek(self):
        return self.top
    def pop(self):
        if self.top==-1:
            return "Under Flow"
        poped=self.array[self.top]
        self.array[self.top]=0
        self.top-=1
        return poped
    def print_link_list(self):
        for i in range(self.len):
            print(self.array[self.len])



