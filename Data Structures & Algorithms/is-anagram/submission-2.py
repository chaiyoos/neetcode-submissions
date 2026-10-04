class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s=s
        self.t=t
        l=sorted(s)
        m=sorted(t)
        if l==m:
            return True
        else:
            return False