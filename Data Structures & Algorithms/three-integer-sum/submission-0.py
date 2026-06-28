class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n):
            target=-nums[i]
            if i>0 and target==-nums[i-1]:
                continue

            l,r=i+1,len(nums)-1
            while l<r:
                sum=nums[l]+nums[r]
                if sum<target:
                    l+=1

                elif sum>target:
                    r-=1
                else:
                    
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    
                    while nums[l] ==nums[l-1] and l<r:
                        l+=1
                    


        return ans

        