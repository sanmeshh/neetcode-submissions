class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        s1="".join(s1)

        l=0
        n=len(s2)
        r=len(s1)
        while r<=n:
            s=s2[l:r]
            s=sorted(s)
            s="".join(s)
            if s==s1:
                return True
            l+=1
            r+=1
        return False

        

            
