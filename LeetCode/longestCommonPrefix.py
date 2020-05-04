#Input: ["flower","flow","flight"]
#Output: "fl"
def longestCommonPrefix(self, strs):
    prefix = []
    for ele in zip(*strs):
        if len(set(ele)) ==1:
            prefix.append(ele[0])
        else:
            break
    return "".join(prefix)
