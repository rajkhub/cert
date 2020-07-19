#LinkedListNthToLast

def linkedListNthtoLast(head,n):
    lp = head
    rp = head
    
    for i in range(n-1):
        rp = rp.nextnode
    
    while rp.nextnode is not None:
        rp = rp.nextnode
        lp = lp.nextnode
    return lp


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

x = linkedListNthtoLast(a,2)
#x.val =4
