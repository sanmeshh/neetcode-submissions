class Solution:
    def maxProfit(self, prices: List[int]) -> int:

            buy=prices[0]
            overall=0
            for r in range(len(prices)):
                if buy>prices[r]:
                    buy=prices[r]
                else:
                    profit=prices[r]-buy
                    overall=max(overall,profit)
            return overall
                    


        