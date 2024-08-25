# Producer ----Queue----- Consumer
# FIFO
# List can be used as queues via arr.insert(0,'Value')
from collections import deque
queue = deque()
queue.appendleft(45)
# print(queue)

class Queue:
    def __init__(self):
        self.container = deque()
    def enqueue(self,val):
        self.container.appendleft(val)
    def dequeue(self):
        return self.container.pop()
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    
pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.container)
print(pq.dequeue())