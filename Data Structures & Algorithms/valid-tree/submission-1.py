class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:#empty tree is valid
            return True

        adjlist={c:[] for c in range(n)}

        for node1,node2 in edges:
            adjlist[node1].append(node2)
            adjlist[node2].append(node1)
        

        visited=set()
        def dfs(node,prev):

            if node in visited:
                return False
            
            visited.add(node)

            for newnode in adjlist[node]:
                if newnode==prev:
                    continue#since we are appending the both edges in adjlist
                    #we have to skip the same edges like 1,0 and 0,1
                
                if not dfs(newnode,node):
                    return False
            return True#base case

        return dfs(0,-1) and n==len(visited)#0 se bas aise hi start krre
        

        

        
        
                











        