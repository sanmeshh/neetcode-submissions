class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        
        
        def findcombination(idx,nums,ds,target):
       
            if target==0:
                ans.append(ds.copy())#since the value of ds changes continuosly we just return its value at that specific instance
                return 

            if idx==len(nums):
                if target==0:
                    ans.append(ds.copy())
                else:
                    return
            
            if(nums[idx]<=target):#our target keeps changing this eg target-arr[idx] thus, we are checking if our new elem is less than the curr target
                ds.append(nums[idx])
                findcombination(idx,nums,ds,target-nums[idx])
                ds.pop(-1)
            findcombination(idx+1,nums,ds,target)
        findcombination(0,nums,[],target)
        return ans


            
        