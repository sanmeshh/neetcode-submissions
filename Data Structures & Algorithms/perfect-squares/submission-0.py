class Solution:
    def numSquares(self, n: int) -> int:

        dp=[n]*(n+1)
        sqs=[]
        for i in range(1,n+1):

            if i*i>n:
                break

            sqs.append(i*i)

        dp[0]=0
        for val in range(1,n+1):
            for s in sqs:
                if val-s<0:
                    break
                dp[val]=min(dp[val],1+dp[val-s])

   
        return dp[n]
        
           

        
        



        