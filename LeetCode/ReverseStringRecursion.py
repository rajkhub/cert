#Reverse a Strin using Recursion
def reverse(s):
    if len(s) <= 1:
        return s
    print s[1:]
    # Recursion
    return reverse(s[1:]) + s[0]

reverse('RAJAs')
