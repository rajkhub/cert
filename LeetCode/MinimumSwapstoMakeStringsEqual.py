# Example 1:

# Input: s1 = "xx", s2 = "yy"
# Output: 1
# Explanation: 
# Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

# Example 2: 

# Input: s1 = "xy", s2 = "yx"
# Output: 2
# Explanation: 
# Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
# Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

# Example 3:

# Input: s1 = "xx", s2 = "xy"
# Output: -1


class Solution(object):
    def minimumSwap(self, s1, s2):
        x1 = 0
        y1 = 0
        
        for i in range(len(s2)):
            if s1[i] != s2[i] and s1[i] == 'x':
                x1 += 1
            if s1[i] != s2[i] and s1[i] =='y':
                y1 +=1
            
        if (x1 +y1)%2 !=0 :
            return -1
                
        # 1 swap(Even) and 2 Swap(odd)
        return x1//2 + y1//2 + x1%2 + y1%2
