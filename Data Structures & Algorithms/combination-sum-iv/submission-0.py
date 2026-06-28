class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:


        dp=[0]*(target+1)
        dp[0]=1
        for val in range(1,target+1):
            
            for n in nums:
                idx=val-n
                if idx>=0:
                    dp[val]+=dp[idx]
        return dp[target]









        


        