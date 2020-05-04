name='malayalam'
def palindrome(name):
    rev = name[::-1]
    if rev == name:
        print "Palin"
    else:
        print "No"
        
def palin2(name):
    for i in range(0,len(name)/2):
        if name[i] == name[len(name)-1-i]:
            return "palin"
        else:
            return "No"
