s = "RAJASEKHAR"
def revString(s):
    x = []
    y = []
    for ele in s:
        x.append(ele)
    for ele in s:
        y.append(x.pop())
    return "".join(y)
    
revString(s)
