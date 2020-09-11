from queue import Queue
from binary_search_tree import BSTNode
from sll import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = Queue()
        self.stored = 0
        self.buffer = []

    def append(self, item):
        if self.stored >= self.capacity:
            self.storage.dequeue()
            self.storage.enqueue(item)
        else:
            self.storage.enqueue(item)
            self.stored += 1
        
      
            

    def get(self):
        temp = self.storage
        items = []
        
        while len(temp) != 0:
            items.append(temp.dequeue())
        
        return items
        