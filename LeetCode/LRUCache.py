#Dcitionary in Python 3 works. In Python we require OrderedDict
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        if key not in self.cache:
            return -1
        
        v = self.cache[key]
        del self.cache[key]
        self.cache[key] = v
        return v
        

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        else:
            if len(self.cache.keys()) >= self.capacity:
                del self.cache[next(iter(self.cache.keys()))]
                # del self.cache[list(self.cache.keys())[0]]
                
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
