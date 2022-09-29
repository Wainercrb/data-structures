'''stacks && queues'''

### Definition ####
# They are both data collections
# 
# 1. The last element added to the stack will be the first item removed 
# 2. Stacks are using for manage functions invocations and undo/redo, routing
# 3. LIFO(last in, first out)
# 4. For the arrays always use push and pop for stacks

### BIG O ####
# Insertion: O(1)
# Removal: O(1)
# Searching: O(N)
# Access: O(N)


class Node(): 
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0


    def push(self, val):
        new_node = Node(val)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.first
            self.first = new_node
            self.first.next = temp
        
        self.size += 1

        return self.size


    def pop(self):
        if not self.first:
            return None
        temp = self.first   

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.size -= 1

        return temp.val


    def print_all_values(self):
        current = self.first
        for _ in range(self.size):
            print(current.val)
            current = current.next


stack = Stack()
print('push 1 to the stack, return: ', stack.push(1))
print('push 2 to the stack, return: ', stack.push(2))
print('push 3 to the stack, return: ', stack.push(3))
print('-------list all values-----------')
stack.print_all_values()


print('pop item from the stack, return: ', stack.pop())
print('-------list all values-----------')
stack.print_all_values()
