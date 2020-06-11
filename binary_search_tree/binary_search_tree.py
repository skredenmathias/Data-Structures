# class Node:
#     def __init__(self, value=None, next_node)
#         self.value = value
#         self.next_node = next_node

#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def add_to_end(self, value):
#         new_node = Node(value)
#         # What if empty?
#         if not self.head:
#             self.head = new_node
#         # If not?
#         else:
#             # traverse
#             current = self.head
#             while current.get_next() is not None:
#                 current = current.get_next()
            
#             current.set_next(new_node)

#     def remove_from_head(self, value):
#         new_node = Node(value)

#         # if empty
#         if not self.head:
#             return None
#         else:
#             # return the value at current head
#             value = self.head.get_value()
#             # and remove the value at the head + add new head
#             self.head = self.head.get_next()
#         return value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_end(value)
        self.size += 1

    def dequeue(self):
        a = self.storage.remove_from_head()
        if a is None:
            return
        else:
            self.size -= 1
            return a

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
        
    def push(self, value):
        # add to head
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            a = self.storage.remove_from_head(value)
            self.size -= 1
            return a
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value

        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target >= self.value and self.right is not None:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)

        # if self.left:
        #     if self.left is None:
        #         return fn(self.value)
        #     else:
        #         fn(self.left)
        # else:
        #     if self.right is None:
        #         return fn(self.value)
        #     else:
        #         fn(self.right)
                ####
        # if self.left:
        #     return fn(self.left.value)
        # else:
        #     return fn(self.right.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            self.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # stack


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_end(value)
        self.size += 1

    def dequeue(self):
        a = self.storage.remove_from_head()
        if a is None:
            return
        else:
            self.size -= 1
            return a

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
        
    def push(self, value):
        # add to head
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            a = self.storage.remove_from_head(value)
            self.size -= 1
            return a

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
