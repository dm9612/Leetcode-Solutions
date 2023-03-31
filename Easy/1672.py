class Solution:
    def maximumWealth(self, accounts):
        highest = 0
        for account in accounts:
            current = sum(account)
            if current > highest:
                highest = current
        return highest
            
