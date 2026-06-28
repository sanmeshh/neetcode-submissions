class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache={}
        n=len(nums)
        def dfs(i,curSum):

            if (i,curSum) in cache:

                return cache[(i,curSum)]

            if i>=n:
                if curSum==target:
                    return 1
                else:
                    return 0
            
            cache[(i,curSum)]=dfs(i+1,curSum+nums[i])+dfs(i+1,curSum-nums[i])
            
            return cache[(i,curSum)]

        return dfs(0,0)
        




        
        