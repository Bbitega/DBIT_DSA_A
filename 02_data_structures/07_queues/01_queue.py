from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    # insert item in the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove the first item
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()

    # check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # check number of items in the queue
    def size(self):
        return len(self.queue)



q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print("Dequeued:", q.dequeue())

print("Check if Queue is empty:", q.is_empty())
