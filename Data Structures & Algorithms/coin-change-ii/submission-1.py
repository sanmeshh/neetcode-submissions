class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp=[0]*(amount+1)
        dp[0]=1

        for coin in coins:
            for amt in range(1,amount+1):
    
                idx=amt-coin
                if idx>=0:
                    dp[amt]+=dp[idx]


        return dp[-1]

        
        