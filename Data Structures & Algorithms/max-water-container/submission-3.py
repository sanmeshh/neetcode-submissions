class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l=0
        n=len(heights)
        r=n-1
        overall=0
        while l<r:
            area=(r-l)*min(heights[l],heights[r])
            overall=max(overall,area)
            #we will increment l,r when we want larger height since for that
            #we are sacrificing our distance
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            

        return overall

            



        
        