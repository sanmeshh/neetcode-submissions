class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj=defaultdict(list)

        tickets.sort()

        for src,tar in (tickets[::-1]):
            adj[src].append(tar)
        res=[]
        def dfs(src):

            while adj[src]:
                nxt=adj[src].pop()
                dfs(nxt)
            res.append(src)

        dfs('JFK')
        res.reverse()
        return res
        

        

                
                
        





        









        




        