class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        n=len(nums)
        nums.sort()

        for i in range(n):
            target=-nums[i]
            if i>0 and target==-nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
               
                summ=(nums[l]+nums[r])
                if summ<target:
                    l+=1
                elif summ>target:
                    r-=1
                else:
                    arr=[nums[i],nums[l],nums[r]]
                    ans.append(arr)
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans


        