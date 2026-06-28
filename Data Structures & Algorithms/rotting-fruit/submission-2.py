class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m,n=len(grid),len(grid[0])
        fresh=0#edge case is that the fresh fruit is not accessible to 
        #the rotten ones then there are non-zero fresh fruits
        q=deque()
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh+=1

                if grid[r][c]==2:
                    q.append([r,c])
                     #getting the initial sources for multisource bfs

        minutes=0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            minutes+=1
        
        return minutes if fresh==0 else -1


        


        

        