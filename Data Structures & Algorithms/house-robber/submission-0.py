class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[0]=nums[0]
        if n>=2:
            dp[1]=nums[1]
        else:
            return nums[0]
        if n>=3:
            dp[2]=nums[2]+nums[0]

        
        for i in range(3,n):
            dp[i]=nums[i]+max(dp[i-2],dp[i-3])
        
        return max(dp[-1],dp[-2])

        
    

        



        
        