class Solution:
    def containsDuplicate(self, nums):
        h = set() 
        for i in range(len(nums)):
            if nums[i] in h:
                return True
            else:
                h.add(nums[i])
        return False
