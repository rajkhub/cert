A=[[1,2,3],[4,5],[6,7,8]]

def rec(a):
   if any(a):
       res = []
       for lst in a[::-1]:
           if len(lst):
               p = lst.pop()
               res.append(p)
       print(res)
       rec(a)

rec(A)
