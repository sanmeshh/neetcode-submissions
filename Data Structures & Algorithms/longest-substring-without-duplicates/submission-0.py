class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=set()
        l=0
        curr=0
        for r in range(len(s)):
            while s[r]  in ans:
                ans.remove(s[l])
                l+=1
            
            
            ans.add(s[r])
            
            curr=max(curr,r-l+1)

        return curr






        


        
            
        