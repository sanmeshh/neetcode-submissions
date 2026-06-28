class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev2,prev=1,1#if couldnt understand see visualization of stairs  and the dp array
       
        for i in range(n,1,-1):
            curri=prev+prev2
            prev2=prev
            prev=curri
        return prev




        