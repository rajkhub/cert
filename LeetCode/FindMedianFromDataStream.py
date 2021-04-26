# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

class MedianFinder(object):

    def __init__(self):
        self.minHeap =[]
        self.maxHeap =[]
        
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        

    def addNum(self, num):
        heapq.heappush(self.maxHeap,-num) #Smaller Half
        
        # Remove element and Add to minHeap
        heapq.heappush(self.minHeap,- self.maxHeap[0])
        heapq.heappop(self.maxHeap) 
        
         #Rebalance- take max element in minHeap and add it to MaxHeap
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap,- self.minHeap[0])
            heapq.heappop(self.minHeap)

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return float(- self.maxHeap[0] + self.minHeap[0])/2
        else:
            return -self.maxHeap[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
