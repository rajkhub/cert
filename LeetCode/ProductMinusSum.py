def productMinusSum(n):
    res =1
    plus =0
    while n>0:
        res = res * (n%10)
        plus = plus + (n%10)
        n = n//10
    return res - plus
    
    
## 1234 - 1+2+3+4 = 14
