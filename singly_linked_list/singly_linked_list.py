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