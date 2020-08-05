class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        if self.stack:
			self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)
        self.stack.append(x)
        

    def pop(self):
        self.stack.pop()
        self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        if len(self.stack) ==0:
            return 0 
        else:
            
            return self.stack[-2]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
