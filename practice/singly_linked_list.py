class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, value: any) -> any:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

        self.length += 1

        return new_node.value


    def pop(self) -> any:

        if not self.head:
            return None

        curr_node = self.head
        prev_node = None

        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = None
        self.tail = prev_node
        self.length -= 1

        return prev_node.value


    def shift(self):
        if not self.head:
            return None

        curr_node = self.head
        next_node = self.head.next
        self.head = next_node
        self.length -= 1

        return curr_node.value

    def unshift(self, value):
        new_node = Node(value)
        self.length += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self.head.value

        new_node.next = self.head
        self.head = new_node
        
        return self.head.value


    def reverse(self) -> bool:

        if not self.head:
            return False 

        curr = self.head.next    
        tail = self.head
        self.head =  self.tail 
        self.tail = tail
        for _ in range(1, self.length):
            temp_curr = curr.next
            curr.next = tail
            tail = curr
            curr = temp_curr
        
        return True

    def __str__(self) -> str:
        curr = self.head
        result = '|'
        
        for _ in range(0, self.length):
            result += f' {curr.value} |'
            curr = curr.next

        return result

SLK = SinglyLinkedList()
SLK.append('1')
SLK.append('2')
SLK.append('3')
SLK.append('4')
SLK.append('5')


print('Printing all the list: ', SLK)
print(f'The head value is: {SLK.head.value}')
print(f'The tail value is: {SLK.tail.value}', end='\n\n\n\n')

print('Pop removed: ', SLK.pop())
print('Printing all the list: ', SLK)
print(f'The head value is: {SLK.head.value}')
print(f'The tail value is: {SLK.tail.value}', end='\n\n\n\n')

print('Shift removed: ', SLK.shift())
print('Printing all the list: ', SLK)
print(f'The head value is: {SLK.head.value}')
print(f'The tail value is: {SLK.tail.value}', end='\n\n\n\n')

print('Unshift removed: ', SLK.unshift('1'))
print('Printing all the list: ', SLK)
print(f'The head value is: {SLK.head.value}')
print(f'The tail value is: {SLK.tail.value}', end='\n\n\n\n')

print('Reversed: ', SLK.reverse())
print('Printing all the list: ', SLK)
print(f'The head value is: {SLK.head.value}')
print(f'The tail value is: {SLK.tail.value}', end='\n\n\n\n')






