class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_tail = Node(value, None)
        if not self.head:
            self.head = new_tail
            self.tail = new_tail

        else:
            self.tail.set_next(new_tail)
            self.tail = new_tail

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.next = None
        return value
    
    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.get_next_node()

        return count

    def contains(self, value):
        current = self.head
        while current.next_node != None:
            if(current.get_value() == value):
                return True
            else:
                current = current.next_node()

        return False
        
            
