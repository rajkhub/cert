def findKthLargest(self, nums, k):
    s = sorted(nums)
    return s[len(nums)-k]

#Using Merge Sort
def findKthLargest(self, nums, k):
    def merge_sort(nums):
        if len(nums)>1:
            mid = len(nums)/2
            first = nums[:mid]
            last = nums[mid:]
            
            merge_sort(first)
            merge_sort(last)
            
            i=0
            j=0
            k=0
            while i< len(first) and j < len(last):
                if first[i]< last[j]:
                    nums[k] = first[i]
                    i +=1
                else:
                    nums[k] = last[j]
                    j +=1
                k +=1
            
            while i < len(first):
                nums[k] = first[i]
                i +=1
                k +=1
            
            while j < len(last):
                nums[k] = last[j]
                j +=1
                k +=1
    merge_sort(nums)            
    print nums
    return nums[len(nums)-k]
