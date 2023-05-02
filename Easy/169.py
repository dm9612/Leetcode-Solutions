class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        i = len(nums)//2

        if len(nums) % 2 == 0:
            res = nums[i-1]
        elif len(nums) == 1:
            return nums[i]

        else:
            res = nums[i]

        return res
