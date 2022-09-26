'''Doubly linked list'''
### Description ####
# Almost identical to Singly Linked List, excep every node has another
# pointer, to the previous node

### Disadvantages compared to singly linked list ###
# 1. Need more momery
# 2. Complex code
# 3. We have two directions, left and rigth

### Advantages compared to singly linked list ###
# 1. Better for findings nodes can be done in half time

#### Big O complexity ###
# - Insertion: O(1)
# - Removal: O(1)
# - Searching: O(N)
# - Access: O(N), technically searching is O(N),but that's still O(N)


import math


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, val):
        new_node = Node(val)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1    
        return self


    def pop(self):
        if self.length == 0:
            return None

        popped_node = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:    
            self.tail = popped_node.prev
            self.tail.next = None
            popped_node.prev = None
        
        self.length -= 1

        return popped_node 


    def shift(self):
        if self.length == 0:
            return None

        old_head = self.head

        if self.length == 0:
            self.head = None
            self.tail = None

        self.head = old_head.next
        self.head.prev = None
        old_head.next = None # remove rest of values to return a single item
        self.length -= 1

        return old_head


    def unshift(self, val):
        new_node = Node(val)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return None


    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None

        middle = math.floor(self.length / 2)

        if idx <= middle:
            count = 0
            current_node = self.head
            while not count == idx:
                current_node = current_node.next
                count += 1
            
            return current_node

        count = self.length - 1
        current_node = self.tail
        while not count == idx:
            current_node = current_node.prev
            count -= 1
        
        return current_node


    def set(self, idx, val):
        find_node = self.get(idx)

        if find_node:
            find_node.val = val
            return True

        return False


    def insert(self, idx, val):
        if idx < 0 or idx > self.length:
            return False 

        if idx == 0:
            return self.unshift(val)
        
        if idx == self.length:
            return self.push(val)

        new_node = Node(val)
        before_node = self.get(idx -1)
        after_node = before_node.next
        before_node.next = new_node
        new_node.prev = before_node
        new_node.next = after_node
        after_node.prev = new_node
        self.length += 1
        return True 


    def remove(self, idx):
        if idx < 0 or idx > self.length:
            return None

        if idx == 0:
            return self.shift()

        if idx == self.length - 1:
            return self.pop()

        removed_node = self.get(idx)
        removed_node.prev.next = removed_node.next
        removed_node.next.prev = removed_node.prev
        removed_node.next = None
        removed_node.prev = None
        self.length -= 1

        return removed_node 


    def print_all_values(self):
        if not self.head:
            return None

        current_head = self.head

        for idx, _ in enumerate(range(0, self.length)):
            print('Indix: #{idx}, value: '.format(idx=idx), current_head.val)
            current_head = current_head.next                              
 

list = DoublyLinkedList()
list.push('item 1')
list.push('item 2')
list.push('item 3')
list.push('item 4')
# list.pop()
# list.shift()
# list.unshift('item unshift')
# get = list.get(4)
# print('-> get', get.val if get else 'No found')
# list.set(0, 'set new value')
# list.insert(3, 'set new value')
# list.remove(2)
list.print_all_values()
