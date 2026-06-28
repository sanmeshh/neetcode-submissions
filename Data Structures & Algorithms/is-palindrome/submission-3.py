import regex as re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        s=re.sub(r'[^a-zA-Z0-9]','',s)
        l=0
        r=len(s)-1
        print(len(s))
        while l<r :
            if s[l]==s[r]:
                l+=1
                r-=1
                print(l,r)
            else:
                return False
        return True
        