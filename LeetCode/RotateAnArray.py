def rotate(arr,k):
    for i in range(k):
        arr.insert(0,arr.pop())
    return arr
rotate([1,2,3,4,5,6,7],3)
