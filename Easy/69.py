class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l<=r:
            m = (l+r)//2
            if m**2 <= x < (m+1)**2:
                return m
            elif m*m>x:
                r = m-1
            else:
                l = m+1
        
        
                
