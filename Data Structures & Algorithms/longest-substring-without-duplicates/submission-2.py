class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        hashset=[]
        ans=0
        l=0
        for r in range(len(s)):
            while hashset and s[r] in hashset:
              
                hashset.remove(s[l])
                l+=1

            hashset.append(s[r])
            ans=max(ans,r-l+1)
            
               
           
        return ans
        
                
