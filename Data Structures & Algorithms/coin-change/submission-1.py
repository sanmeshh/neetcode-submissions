class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=amount


        dp=[10001]*(n+1)
        dp[0]=0

        for amt in range(1,n+1):
            count=0
            for coin in coins:
                idx=amt-coin
                if idx>0:
                    dp[amt]=min(dp[amt],1+dp[idx])
                if idx==0:
                    dp[amt]=1

        return dp[-1] if dp[-1]!=10001 else -1





     




        

        
        