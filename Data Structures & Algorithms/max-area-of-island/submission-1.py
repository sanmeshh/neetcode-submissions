class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        maxarea=0
        def bfs(r,c):
            q=deque()
            grid[r][c] = 0
            q.append((r,c))
            area=0
            while q:
                r,c=q.popleft()
                for ri,ci in directions:
                    row,col=r+ri,c+ci

                    if row>=rows or row<0 or col>=cols or col<0 or grid[row][col]==0:
                        continue
                    q.append((row,col))
                    grid[row][col]=0
                    area+=1
            return area
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area=bfs(r,c)
                    area+=1
                    maxarea=max(maxarea,area)
                
        return maxarea
                
                    
                    
                













        
        for i in range(rows):
            for j in range(cols):
                if grid[i][i]==1:
                    bfs(i,j)




       

        


        