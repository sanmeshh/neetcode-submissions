class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        minheap=[(grid[0][0],0,0)]

        visited=set()
        t=0
        while minheap:
            print(minheap)

            val,i,j=heapq.heappop(minheap)
            t=max(t,val)

            if (i,j) in visited:
                continue
            if i==rows-1 and j==cols-1: 
                break
            visited.add((i,j))
            
           
            

            for dr,dc in directions:
                i1=i+dr
                j1=j+dc
                if i1<0 or i1>=rows or j1<0 or j1>=cols or (i1,j1) in visited:
                    continue
                heapq.heappush(minheap,(grid[i1][j1],i1,j1))
        
        return t
            

            
            

                
                
            

        

            














        
        