def isValid(self, s):
    open =set('{[(')
    all = set( [ ('[',']'), ('{','}'), ('(',')') ] )
   
    x = []
    for ele in s:
        if ele in open:
            x.append(ele)
        else:
            if len(x) == 0:
                return False
            popped = x.pop()
            
            if (popped,ele) not in all:
                return False
        
    if len(x) ==0:
        return True
