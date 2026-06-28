from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist=[]
        maxheap=[]
        for num in points:
            x1=num[0]
            y1=num[1]
            val=-round(sqrt((x1**2)+(y1**2)),3)
            dist.append(val)
            heapq.heappush(maxheap,[val,x1,y1])#heap is maintained acc to the val(first element)
            while len(maxheap)>k:#pops the larger distance thus leaving us with the smaller distances(closest to origin)
                heapq.heappop(maxheap)
        
        ans=[]
        for num in maxheap:
            dist,x,y=num
            ans.append([x,y])
        return ans

            

                   
        

        

        
    
        
    

        