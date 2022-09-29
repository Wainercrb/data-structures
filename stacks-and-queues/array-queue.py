'''stacks && queues'''

### Definition ####
# They are both data collections, we have only two operators, added and removed
# 
# 1. The common example of queue, think in the lobby of some video game, we 
#    have to wait in the lobby to start the game
# 2. When we upload or download something we are using queues, also for 
#    background tasks, printing and tasks processing


queue = []


# Add the items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)


# Remove items from the queue
queue = queue[1:]
queue = queue[1:]
queue = queue[1:]
print(queue)
