from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.strs=strs
        l1=[]
        l2=defaultdict(list)
        for i in strs:
            s=tuple(sorted(i))
            l2[s].append(i)
        for value in l2.values():
            l1.append(value)
        return l1



