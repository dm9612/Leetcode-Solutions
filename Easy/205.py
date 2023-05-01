class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst, mapts = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in mapst and mapst[c1] !=c2) or (c2 in mapts and mapts[c2]!=c1)):
                return False
            mapst[c1] = c2
            mapts[c2] = c1
        return True
        
