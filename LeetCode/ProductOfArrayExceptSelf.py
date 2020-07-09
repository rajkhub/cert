# Product of Array Except Self
#input =[1,2,3,4]
# Output = [24, 12, 8, 6]
arr=[1,2,3,4]
def multiply(arr):
    res = []
    for i in range(len(arr)):
        cnt =1
        for j in range(1,len(arr)):
            if i !=j:
                cnt = cnt * arr[j]
            if j == len(arr)-1:
                res.append(cnt)
    return res
