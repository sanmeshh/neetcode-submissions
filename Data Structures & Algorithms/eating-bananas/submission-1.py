import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l=1
        r=max(piles)
        
        overall=float('inf')
        
        while l<=r:
            k=(l+r)//2
            hours=0
            for b in piles:
                hours+=math.ceil(b/k)
            if hours<=h:
                overall=min(k,overall)
                r=k-1

            else:
                l=k+1
        return overall

                
                

            