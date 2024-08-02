class Solution:
    def average(self, salary: List[int]) -> float:
        min = 1000000
        max = 0
        n = len(salary)
        s = 0

        for i in salary:
            s+=i
            if max < i:
                max = i
            if min > i:
                min = i
        
        return (s-min-max)/(n-2)
