'''stacks && queues'''

### Definition ####
# They are both data collections, we have only two operators, added and removed
# remember LIFO
# 
# 1. The common example of queue, think in the lobby of some video game, we 
#    have to wait in the lobby to start the game
# 2. When we upload or download something we are using queues, also for 
#    background tasks, printing and tasks processing


### BIG O ####
# Insertion: O(1)
# Removal: O(1)
# Searching: O(N)
# Access: O(N)


class Node(): 
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0


    def enqueue(self, val) -> int:
        new_node = Node(val)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1

        return self.size


    def dequeue(self):
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


queue = Queue()
print('enqueue 1 to the stack, return: ', queue.enqueue(1))
print('enqueue 2 to the stack, return: ', queue.enqueue(2))
print('enqueue 3 to the stack, return: ', queue.enqueue(3))
print('-------list all values-----------')
queue.print_all_values()


print('dequeue item from the stack, return: ', queue.dequeue())
print('-------list all values-----------')
queue.print_all_values()
