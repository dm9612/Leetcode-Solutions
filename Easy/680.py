class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return self.Palindrome(s, l+1, r) or self.Palindrome(s, l, r-1)
        return True 

    def Palindrome(self, s, l, r): 
        while l<r:
            if s[l]== s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
