class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        def findcombination(idx,candidates,target,ds):
            if target==0 :
                arr=sorted(ds.copy())
                if arr not in ans:
                    ans.append(arr)
                return
            if idx==len(candidates) or target<0:
                return

            if candidates[idx]<=target:
                ds.append(candidates[idx])
                findcombination(idx+1,candidates,target-candidates[idx],ds)
                ds.remove(candidates[idx])#to try other numbers as well(main logic)
                #is after adding this number the code ends(idx==len or tar<0) then we remove that number
                #from the ds[] and further in the code try new number(if not duplicate)
           
            findcombination(idx+1,candidates,target,ds)
        findcombination(0,candidates,target,[])

        return ans
        



            
                        