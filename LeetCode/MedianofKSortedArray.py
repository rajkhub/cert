 # [-3 -1 0] 4 5 6 7 8   -1
 # -1 [0 -3 4] 5 6 7 8   0
 # -1 0 [-3 4 5] 6 7 8   4
 # -1 0 -3 [4 5 6] 7 8   5 
 # -1 0 -3 4 [5 6 7] 8   6
 # -1 0 -3 4 5 [6 7 8]   7


arr=[-3, -1, 0, 4, 5, 6, 7, 8]
k = 2


def medSort(arr,k):
    res=[]
    for i in range(k,len(arr)+1):
        win =  arr[i-k:i]
        sorted(win)
        mid = len(win)/2
        if len(win)%2 != 0:
            res.append(win[mid])
        else:
            res.append( (win[mid] + win[mid-1])/2)
    print res


medSort(arr,k)
