class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target>nums[m]:
                l = m+1
            elif target<nums[m]:
                r = m-1
            else:
                return m
        return -1
