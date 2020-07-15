#Input: ["flower","flow","flight"]
#Output: "fl"
# Zip Returns
# returns
#         ('f', 'f', 'f')
#         ('l', 'l', 'l')
#         ('o', 'o', 'i')
#         ('w', 'w', 'g')
#         ('e', 'e', 'h')
def longestCommonPrefix(self, strs):
    prefix = []
    for ele in zip(*strs):
        if len(set(ele)) ==1:
            prefix.append(ele[0])
        else:
            break
    return "".join(prefix)
