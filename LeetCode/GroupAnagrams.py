#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]


class Solution(object):
    def groupAnagrams(self, strs):
        d=collections.defaultdict(list)
        for ele in strs:
            s_sort = ''.join(sorted(ele))
            d[s_sort].append(ele)
        return list(d.values())
