# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals)
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
