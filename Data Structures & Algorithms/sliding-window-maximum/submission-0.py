class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l=0
        
        ans=[]
        for r in range(k-1,len(nums)):
            res=max(nums[l:r+1])
            ans.append(res)
            l+=1

        return ans



        