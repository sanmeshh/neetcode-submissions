class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy=0
        minn=float('inf')
        for i in range(len(prices)):
            minn=min(minn,prices[i])
            nbuy=prices[i]-minn
            buy=max(buy,nbuy)
        return buy



        
        