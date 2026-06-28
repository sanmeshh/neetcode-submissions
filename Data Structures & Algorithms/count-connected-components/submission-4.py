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
       
        c=0
        for i in range(n):
            if i not in visited:
                #just mark visited to all unvisited nodes
                stack=[]
                stack.append(i)
                while stack:
                    node=stack.pop()
                    if node not in visited:
                        visited.add(node)
                        for nei in adjlist[node]:
                            if nei not in visited:
                                stack.append(nei)
                c+=1
    
        return c



        


            
            

        