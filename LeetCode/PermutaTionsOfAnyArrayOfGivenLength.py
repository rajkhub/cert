#inp = ['R','B','G']
#num=3
#Ouput = RRR
#RRB
#RRG
#RBR
#RBB


def premu(inp,num):
    iterate(num,inp,"")
    
def iterate(num,inp,prefix):
    if num ==0:
        print(prefix)
        return
    
    for i in range(len(inp)):
        newPrefix = prefix + inp[i]
        
        iterate(num-1,inp,newPrefix)

            
premu(inp,num)
