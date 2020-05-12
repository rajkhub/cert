#Implementation of Stack
class Stack(object):
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
        
x = Stack()
x.push(1)
x.push(2)
x.push(3)
