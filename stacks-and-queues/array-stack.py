'''stacks && queues'''

### Definition ####
# They are both data collections
# 
# 1. The last element added to the stack will be the first item removed 
# 2. Stacks are using for manage functions invocations and undo/redo, routing
# 3. LIFO(last in, first out)
# 4. For the arrays always use push and pop for stacks

### Simple Stack Example ###

# Define out stack as new array
stack = []

# Push the item to the stack
stack.append('1')
stack.append('2')
stack.append('3')
print(stack)

# Remove the last items from the stack, remember LIFO
stack.pop()
stack.pop()
stack.pop()
print(stack)

