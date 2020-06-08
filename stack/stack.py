"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Node:
    def __init__(self, value=None, next_node)
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self, head):
        self.head = None

    def add_to_end(self, value):
        new_node = Node(value)
        # What if empty?
        if not self.head:
            self.head = new_node
        # If not?
        else:
            # traverse
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            
            current.set_next(new_node)

    def remove_from_head(self, value):
        new_node = Node(value)

        # if empty
        if not self.head:
            return None
        else:
            # return the value at current head
            value = self.head.get_value()
            # and remove the value at the head + add new head
            self.head = self.head.get_next()
        return value

    def add_to_head(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            # do we want to save the old head?
            head = self.head #2
            # wrap + set as new head
            self.head = Node(value) #1
            # add pointer to next node
            self.head.next_node = head

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        pass

    def push(self, value):
        # self.storage.insert(0, value)
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if len(self.storage) > 0:
            a = self.storage.pop() # 0
            self.size -= 1
            return a

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass
