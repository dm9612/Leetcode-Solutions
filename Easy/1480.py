class Solution:
    def runningSum(self, nums):
        a = 0
        lst=[]
        for i in nums:
            a = a+i
            lst.append(a)
        return(lst)
