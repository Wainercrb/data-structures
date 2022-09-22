'''Singly linked list basics'''

#### Big O complexity ###
# - Insertion: O(1)
# - Removal - it depends: O(1) or O(N)
# - Searching: O(N)
# - Access: O(N)

### Important! #####
# 1. Singly-list are excellent alternative  to arrays when insertion and deletion
#    at the beginning are frequently required.
# 2. Singly-list does not require index, it works under nodes


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


# Example how the node class works
first = Node('Node 1')
first.next = Node('Node 2')
first.next.next = Node('Node 3')
first.next.next.next = Node('Node 4')


class Singly_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.print_values()


    def push(self, val):
        new_node = Node(val)

        if not self.head: # the list is empty
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return self


    def pop(self):
        if not self.head:
            return None
        
        current = self.head
        new_tail = current
        
        while current.next:
            new_tail = current
            current = current.next

        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return current


    def shift(self):
        if not self.head:
            return None

        current_head = self.head
        self.head = current_head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return current_head


    def unshift(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return self


    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        
        current_head = self.head
        for _ in range(0, idx):
            current_head = current_head.next

        return current_head


    def set(self, idx, val):
        node = self.get(idx)

        if not node:
            return False

        node.val = val # replace the value by reference

        return True


    def insert(self, idx, val):
        if idx < 0 or idx > self.length:
            return False

        if idx == self.length:
            self.push(val)
            return True
        
        if (idx == 0):
            self.unshift(val)
            return True

        new_node = Node(val)
        prev_node = self.get(idx - 1)
        tem_node = prev_node.next
        prev_node.next = new_node
        new_node.next = tem_node
        self.length += 1

        return True


    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None

        if idx -1 == self.length:
            return self.pop() 

        if idx == 0:
            return self.shift()

        prev_node = self.get(idx - 1)
        removed_node = prev_node.next
        prev_node.next = removed_node.next
        self.length -= 1
        
        return removed_node 


    def reverse(self):
        if not self.head:
            return None

        node = self.head
        self.head = self.tail
        self.tail = node
        next_node = None
        prev_node = None

        for _ in range(self.length):
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return self 


    def print_values(self):
        if not self.head:
            return None

        current_head = self.head

        for idx, _ in enumerate(range(0, self.length)):
            print('Indix: #{idx}, value: '.format(idx=idx), current_head.val)
            current_head = current_head.next    


list = Singly_linked_list()
list.push('item 1')
list.push('item 2')
list.push('item 3')
list.push('item 4')
list.push('item 5')
list.pop()
list.shift()
list.unshift('item 6')
list.set(1, 'item replaced')
list.insert(1, 'insert #2 position')
list.remove(1)
list.reverse()
list.print_values()
print(list.get(2).val)