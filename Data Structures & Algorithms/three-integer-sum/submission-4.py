class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            target=-(nums[i])
            l=i+1
            r=len(nums)-1
        
            while l<r:
                x=nums[l]+nums[r]
                if x>target:
                    r-=1
                elif x<target:
                    l+=1
                else:
                    lst=[nums[i],nums[l],nums[r]]
                    if lst not in ans:
                        ans.append(lst)
                    
                    l+=1
                    r-=1
                    
        return ans

