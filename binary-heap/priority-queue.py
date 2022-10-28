'''Priority Queue:

Description: A data structure where each element has a priority. Elements 
with higher priorities are served before elements with lower priorities,the
priority queue are separate from heaps
'''

from math import floor

class Node():
  def __init__(self, value, priority) -> None:
    self.value = value
    self.priority = priority


class MaxBinaryHeap():
    def __init__(self) -> None:
        self.values = []


    def enqueque(self, value, priority):
        new_node = Node(value, priority)
        self.values.append(new_node)
        self.bubble_up() 
        
    
    def bubble_up(self):
        '''swap the values until we found the correct place'''
        
        idx = len(self.values) - 1
        ele = self.values[idx] # Last element from values

        while idx > 0:
            parent_idx = floor((idx - 1) / 2)
            parent = self.values[parent_idx]
            
            if ele.priority <= parent.priority: break

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

          if left_child.priority > ele.priority:
            swap = left_child_idx

        if right_child_idx < length:
          right_child = self.values[right_child_idx]

          if (swap is None and right_child.priority > ele.priority) or \
             (swap is not None and right_child.priority > left_child.priority):
            
            swap = right_child_idx
      
        if not swap: break

        self.values[idx] = self.values[swap]
        self.values[swap] = ele
        idx = swap

    def print_list(self):
      for i in self.values:
        print(f'value: {i.value}, priority: {i.priority}', end=' | ')
      print('\n====================================')        


er = MaxBinaryHeap()
er.enqueque('P2', 2)
er.print_list()
er.enqueque('P1', 1)
er.print_list()
er.enqueque('P3', 3)
er.print_list()

