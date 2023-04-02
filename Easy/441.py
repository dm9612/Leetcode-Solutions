class Solution:
    def arrangeCoins(self, n):
        l,r = 1, n
        res = 0
        while l<=r:
            m = (l+r)//2
            c = (m/2)*(m+1)
            if c>n:
                r = m-1
            else:
                l = m+1
                res = max(m,res)
        return res
        

