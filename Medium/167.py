class Solution:
    def twoSum(self, numbers, target):
        l, h = 0, len(numbers) -1
        while l<h:
            cursum = numbers[l]+numbers[h]
            if cursum > target:
                h= h-1
            elif cursum <target:
                l = l+1
            else:
                return [l+1,h+1]
        return []
