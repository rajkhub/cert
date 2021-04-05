from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity
        

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
        

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)
            
# Complexity Analysis
# Time complexity : \mathcal{O}(1)O(1) both for put and get since all operations with ordered dictionary : get/in/set/move_to_end/popitem (get/containsKey/put/remove) are done in a constant time.
# Space complexity : \mathcal{O}(capacity)O(capacity) since the space is used only for an ordered dictionary with at most capacity + 1 elements.
