class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        water=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            water=max(water,area)
            
            
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
                r-=1


        return water





        