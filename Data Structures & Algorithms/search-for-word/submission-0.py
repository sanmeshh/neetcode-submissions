class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hashset=set()
        m=len(board)
        n=len(board[0])
        
        level=0
        def search(i,j,level):
    
            if len(word)==level:
                
                return True

            if i>=m or i<=-1 or j>=n or j<=-1 or board[i][j]!=word[level] or (i,j)  in hashset:
                return False
           

            hashset.add((i,j))

            res=(search(i,j+1,level+1) or
            search(i+1,j,level+1) or
            search(i,j-1,level+1) or
            search(i-1,j,level+1))
            hashset.remove((i,j))
            return res
        
        for i in range(m):
            for j in range(n):
                if search(i,j,0):#taking each element as the starting node
                    return True
        return False

      

     
                

                
           
            