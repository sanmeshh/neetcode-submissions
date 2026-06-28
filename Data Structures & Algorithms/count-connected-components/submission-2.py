class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if n==0:
            return 0
        adjlist={i:[] for i in range(n)}
        visited=set()
        for n1,n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        
        def dfs(node):
  
            
            visited.add(node)
            
            for n1 in adjlist[node]:
    
                
                if n1 not in visited:
                    dfs(n1)
            
        c=0
     
        for i in range(n):

           
            if i not in visited:
                dfs(i)
                c+=1
    
        return c



        


            
            

        