class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=[c for c in s if c.isalnum()]

        n=len(s)
        l=0
        r=n-1
        
        while(l<r):
            if s[l]!=s[r]:
                return False
                
            else:
                l+=1
                r-=1

        return True

        
        