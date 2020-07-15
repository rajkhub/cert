# 2nd Min element in Array
arr=[54,41,41,32,22,0,4,3,4,2,1,1]

def secmin(arr):
    minele = float('inf')
    secele = float('inf')
    
    for i in range(0,len(arr)):
        if minele > arr[i]: 
            secele = minele
            minele = arr[i]
        else:
            secele = arr[i]
    return secele

secmin(arr)
