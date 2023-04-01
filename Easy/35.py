class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                return m
        return l
