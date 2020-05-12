#Implementation of Queue
class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def deque(self):
        self.items.pop()
    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
