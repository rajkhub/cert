#Inp = 123
#out = 321
#In = 120
#out = 21

def reverse(self, x):
    if x>=0:
        x = int(str(x)[::-1])
    else:
        print str(-x)
        x= -int(str(-x)[::-1])
    return x if x<=(2**31-1) and x>=-(2**31) else 0 


def reverse(number):
    rev = 0
    while number>0:
        n = number%10
        rev = rev*10 + n
        number = number//10
    return rev
