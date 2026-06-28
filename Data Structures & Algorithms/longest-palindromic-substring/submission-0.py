class Solution:
    def longestPalindrome(self, s: str) -> str:
        #not a dp soln
        res=''
        reslen=0

        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1

                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1

                l-=1
                r+=1
        
        return res
        


       # If the code didn't check both at every index, it might miss the longest palindrome simply because it was looking for the wrong "shape" (odd vs. even).

        

        

            




        
        