class Solution:
    def twoSum(self, nums, target):
        dict ={}
        for i, value in enumerate(nums):
            requirednum = target - value

            if requirednum in dict:
                return [dict[requirednum], i]
            else:
                dict[value] = i
        
