class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()

        res=0
        res2=0
        for i in range(len(nums)+1):
            res2=res2^i
        for i in range(len(nums)):
            res=res^nums[i]
            
        return res^res2
        
    
        return res
            






        