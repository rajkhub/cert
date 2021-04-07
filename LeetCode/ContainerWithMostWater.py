# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

class Solution(object):
    def maxArea(self, height):
        l = 0 
        r = len(height)-1
        maxv = float('-inf')
        while l < r:
            diff = r - l 
            areaval = min(height[r],height[l])  
            maxv = max(maxv,diff*areaval )
            
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        return maxv
