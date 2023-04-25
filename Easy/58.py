class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i-=1
        while s[i]!= " " and i>=0:
            length+=1
            i-=1
        return length
