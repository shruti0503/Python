stack=[]
#append () function to push element in the stack 
stack.append('1')
stack.append('2')
stack.append('3')

print('Initial stack')
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)


############################

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
stack=[]
#append () function to push element in the stack 
stack.append('1')
stack.append('2')
stack.append('3')

print('Initial stack')
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

#implimenting using queue module 
#LIFO queue , -> basically a stack
#data inserted into quweuw using the put () function and get() takes data out from the queue

# function in. this mouduole maxsize(), empty(), full(), get(), get(item)
#get_nowwait() put(item) put_nowait(item)

from queue import LifoQueue
stack=LifoQueue(maxsize=3)
print("stack size is ",stack.qsize())
stack.put('1')
stack.put('2')

print ("Full :", stack.full()) # gives false
print("size:", stack.qsize())

#get() function to pop

print("Element popped from the stack")
print(stack.get())
print(stack.get())
print(stack.get())

print(stack.empty())

####################
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Stack:
    #stack initialisation
    #using a dummy node , easie for handling edge cases
    def __init__(self):
        self.head=Node("head")
        self.size=0
    
    def __str__(self):
        cur=self.head.next
        out=""
        while cur:
            out +=str(cur.value)+ "->"
            curr=cur.next
        return out[:-2]
    
    #Get the current size of the stack
    def getSize(self):
        return self.size
        
    def isEmpty(self):
        return self.size==0
    
    def peek(self):
        #sanitary check to see if we are peeking an emppty stacl
        
        if self.isEmpty():
            raise Exception("peeking from an empty stack")
        return self.head.next.value
      
    #push value in stack  
    def push(self, value):
        node=Node(value)
        node.next=self.head #make the new node point to the current head
        self.head=node #update the head to be the new node
        self.size+=1
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an emppty stack")
        remove=self.head.next
        self.head.next=self.head.next
        self.size-=1
        return remove.value
        
