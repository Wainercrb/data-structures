from utils import print_tree
from collections import deque

'''Trees'''
### Definition ###
# A data structure that consists of nodes in a parent/child relationship
# The trees are not linear
#
# 1. ROOT: The top node in a tree
# 2. CHILD: A node directly connected to another node when moving away from
#           the root
# 3. PARENT: the converse notion of a child
# 4. SIBLINGS: A group of nodes with the same parent
# 5. LEAF: A node with no children

### Use Cases ###
# 1. HTML DOM nodes
# 2. Routing network
# 3. Programing diagram(UML)
# 4. Abstract syntax trees(the programing languajes works as trees structure)
# 5. Folder structure in your machine
# 6. JS Json's

### Binary Trees Rules ###
# 1. The parent only can have 2 children's
# 2. Every node to the left of a parent node is ALWAYS LESS than the parent
# 3. Every node to the left of a parent node is ALWAYS GREATER than the parent

# Time Complexity
# Insert - O(log n)
# Searching - O(log n)


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    

    def insert(self, value):
        new_node = Node(value)
        
        if not self.root:
            self.root = new_node
            return self

        current = self.root

        while True:
            if value == current.value:
                return None

            if value < current.value:
                if not current.left:
                    current.left = new_node
                    return self
                else: 
                    current = current.left
            elif value >  current.value:
                if not current.right:
                    current.right = new_node
                    return self
                else:
                    current = current.right


    def find(self, value):
        if not self.root:
            return False

        current = self.root
        found = False

        while found == False and current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
        return current if found == True else False

    def BFS(self):
        '''Breadth First Search'''
        node = self.root
        data  = deque([])
        queue = deque([])
        queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()
            data.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return data

    def DFS_pre_order(self):
        '''Depth First PreOrder:
        
        Description: Gets the nodes values from top to bottom
        '''

        nodes_visited = []

        def traverse(node):
            nodes_visited.append(node.value)
            
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            
        traverse(self.root)

        return nodes_visited

    def DFS_post_order(self):
        '''Depth First PostOrder
        
        Description: Gets the nodes values from bottom to top'''
        data = []

        def traverse(node):
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            data.append(node.value)
        
        traverse(self.root)
        
        return data

    def BFS_in_order(self):
        '''Depth First Inorder
        
        Description: Gets the values from the children's to the root'''
        data = []

        def traverse(node):
            if node.left: traverse(node.left)
            
            data.append(node.value)

            if node.right: traverse(node.right)

        traverse(self.root)

        return data


bst = BinarySearchTree()
bst.insert(10)
bst.insert(6)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(10)
print(bst.BFS())
print(bst.find(11))
print_tree(bst.root)  
print(bst.DFS_pre_order())
print(bst.DFS_post_order())
print(bst.BFS_in_order())

