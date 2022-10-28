'''Binary Heap

Description: 
- Very similar to a BINARY SEARCH TREE, but with some diff rules.
- In a MaxBinaryHeap, parent nodes are always larger than child nodes, in a 
  MinBinaryHeap, parent nodes are always similar smaller than child nodes

MAX BINARY HEAP:
- Each parent has at most two child nodes
- The value of each parent node is always greater than its child nodes
- In a max binary heap the parent is greater than the children, but there are
  no guarantees sibling nodes
- A binary heap is as compact as possible. All the children of each node are 
  as full as they can be and left children are filled out first

BIG O

Insertion: O(log N)
Removal: O(log N)
Search: O(N)

RECAP
1. Binary Heaps are very useful data structure for sorting and implementing
   other data structure like PRIORITY QUEUES
2. Binary heaps are either MaxBinaryHeap or MinBinaryHeap with parent either
   being smaller or larger that their children
'''

from math import floor

class MaxBinaryHeap():
    def __init__(self) -> None:
        self.values = [41, 39, 33, 18, 27, 12]
        # self.values = []


    def insert(self, value):
        self.values.append(value)
        self.bubble_up() 


    def bubble_up(self):
        '''swap the values until we found the correct place'''
        
        idx = len(self.values) - 1
        ele = self.values[idx] # Last element from values

        while idx > 0:
            parent_idx = floor((idx - 1) / 2)
            parent = self.values[parent_idx]
            
            if ele <= parent: break

            self.values[parent_idx] = ele
            self.values[idx] = parent
            idx = parent_idx


    def extract_max(self):
      '''SINK DOWN: The procedure for deleting the root from the heap'''

      max_ele = self.values[0]
      end_ele = self.values.pop()
      self.values[0] = end_ele
      self.sink_down()

      return max_ele

    
    def sink_down(self):
      '''Actions:
      1. Remove the top ele
      2. Move the last ele to the top
      3. Re-order the array'''

      idx = 0
      length = len(self.values)
      ele = self.values[0]

      while True:
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        right_child, left_child, swap = None, None, None

        if left_child_idx < length:
          left_child = self.values[left_child_idx]

          if left_child > ele:
            swap = left_child_idx

        if right_child_idx < length:
          right_child = self.values[right_child_idx]

          if (swap is None and right_child > ele) or \
             (swap is not None and right_child > left_child):
            
            swap = right_child_idx
      
        if not swap: break

        self.values[idx] = self.values[swap]
        self.values[swap] = ele
        idx = swap  


heap = MaxBinaryHeap()
heap.insert(55)
print(heap.extract_max())
print(heap.extract_max())
print(heap.extract_max())
print(heap.extract_max())




