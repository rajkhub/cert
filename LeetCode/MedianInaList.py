#Median of a list

def median(lst):
    ln = len(lst)
    mid = len(lst)/2

    
    if ln%2 !=0:
        return lst[mid]
    else:
        return (lst[mid-1] +lst[mid])/float(2)
    
lsat = [1,2,3,4,5]
x = median(lsat)
print x 
lst = [4, 5, 8, 9, 10, 17]
median(lst)
