#arra based implimantation:
import numpy as np
class Queue:
    def __init__(self,len):
        self.queue=np.zeros(len)
        self.length=len
        self.out_point=-1
        self.entry_point=0
    def enqueue(self,data):# data entry
        if self.entry_point==self.out_point:
            return "Over_Load"
        self.queue[self.entry_point]=data
        self.entry_point=(self.entry_point+1)%(self.length)
        if self.out_point==-1:
            self.out_point+=1
    def dequeue(self):
        if self.out_point==-1:
            return "Under_bound"
        pop_item=self.queue[self.out_point]
        self.queue[self.out_point]=0
        self.out_point=(self.out_point+1)%(self.length)
        if self.out_point==self.entry_point:
            self.out_point=-1
            self.entry_point=0
        return pop_item
    def  peek(self): #only shows the first item of the queue, doesnt remove anything
        if self.out_point==-1:
            return "Under_bound"
        else:
            return self.queue[self.out_point]


## Link_list_based implimatation:


        
