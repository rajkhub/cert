# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2


class Solution(object):
    def minMeetingRooms(self, intervals):
        # sort
        intervals.sort(key = lambda interval:interval[0])
        
        roomsUsed=[]
        # create heapq to store the miimum of end times
        heapq.heappush(roomsUsed,intervals[0][1])
        
        for i in range(1,len(intervals)):
            if roomsUsed[0] <= intervals[i][0]:
                heapq.heappop(roomsUsed)
            heapq.heappush(roomsUsed,intervals[i][1])
        return len(roomsUsed)
            
            
        
