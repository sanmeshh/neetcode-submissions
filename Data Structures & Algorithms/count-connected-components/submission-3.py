class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       
        adjlist={i:[] for i in range(n)}
        visited=set()

        #we'll just apply a dfs algo on each node till a component ends
        #cuz we have all the nodes present 'n' so we'll run a loop
        #if they not a visited it means we got a new component

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
                dfs(i)#just mark visited to all unvisited nodes
                c+=1
    
        return c



        


            
            

        