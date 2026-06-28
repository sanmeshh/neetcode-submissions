class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS,COLS=len(grid),len(grid[0])
        visited=set()
        q=deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    visited.add((i,j))
                    q.append((i,j))
        
        def addroom(r,c):

            if (r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited
                 or grid[r][c]==-1):
                 return
                
                
            
            visited.add((r,c))
            q.append((r,c))
                
        dist=0
        while q:
            for i in range(len(q)):#length at that point of traversal
                r,c=q.popleft()
                grid[r][c]=dist
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)

            dist+=1

        
             










        