class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None
class enqueue:
    def __init__(self, max_size):
        self.head=None
        self.last=None
        self.max_size=max_size
        self.count=0
    def insert(self, data):
        n_node=Node(data)
        if self.head is None:
            self.head=n_node
            self.last=n_node
            return
        else:
            self.count=0
            node=self.head
            while node!=self.last:
                self.count=self.count+1
                node=node.ref
            if self.count+1>self.max_size-1:
                return print("Queue is full")
            self.last.ref=n_node
            n_node.ref=self.head
            self.last=n_node
    def dequeue(self):
        if self.head is None:
            return print("No elements in the list. So nothing deleted")
        node=self.head
        self.last.ref=node.ref
        self.head=node.ref  
    def p_q(self):
        node=self.head
        while node!=self.last:
            print(node.data)
            node=node.ref
        print (self.last.data)
a  = enqueue(4)
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.p_q()
a.insert(5)
print("delete")
a.dequeue()
a.p_q()
 
#Code for queue:-
class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None
class enqueue:
    def __init__(self):
        self.head=None
        self.last=None
    def insert(self, data):
        n_node=Node(data)
        if self.head is None:
            self.head=n_node
            self.last=n_node
            return
        else:
            node=self.head
            self.last.ref=n_node
            n_node.ref=self.head
            self.last=n_node
 
    def p_q(self):
        node=self.head
        while node!=self.last:
            print(node.data)
            node=node.ref
        print (self.last.data)
a  = enqueue()
a.insert(1)
a.insert(2)
a.insert(3)
a.p_q()
 
#Code for dequeue:-
# Python program to demonstrate queue implementation using collections.dequeue
from collections import deque
# Initializing a queue
q = deque()
# Adding elements to a queue
q.append('10')
q.append('20')
q.append('30')
print("Initial queue")
print(q)
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)
