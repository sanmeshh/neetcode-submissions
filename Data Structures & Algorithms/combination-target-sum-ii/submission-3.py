class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        candidates.sort()
        def findcombination(idx,candidates,target,ds):
           
            if target==0 :
                
                ans.append(ds.copy())
               
                return
            if idx==len(candidates) or target<0:
                return

            if candidates[idx]<=target:
                ds.append(candidates[idx])
                findcombination(idx+1,candidates,target-candidates[idx],ds)
                ds.pop(-1)#to try other numbers as well(main logic)
                #is that after adding this number the code ends(idx==len or tar<0) then we remove that number
                #from the ds[] and further in the code try new number(if not duplicate)

            while idx+1<len(candidates) and candidates[idx]==candidates[idx+1]:
                idx+=1        
            findcombination(idx+1,candidates,target,ds)
        findcombination(0,candidates,target,[])
     
        return ans
        



            
                        