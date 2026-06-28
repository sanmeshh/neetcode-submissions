class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
            
        slow2=0
        while True:
        #distance bw the start of the LL is same as between meeting point of (fast and slow) 
        #and the number after start of the cycle
            slow=nums[slow]
            slow2=nums[slow2]
            if slow == slow2:
                return slow

            

        


        