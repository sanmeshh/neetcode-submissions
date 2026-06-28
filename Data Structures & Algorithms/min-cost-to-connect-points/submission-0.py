class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adjlist={i:[] for i in range(n)}
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                #mapping thru index in points list
                adjlist[i].append([dist,j])
                adjlist[j].append([dist,i])#undirected
        visited=set()
        minheap=[[0,0]]#cost,point   
        res=0

        #prims
        while len(visited)<n:
            cost,point=heapq.heappop(minheap)
            if point in visited:
                continue
            
            res+=cost
            visited.add(point)
            for neicost,nei in adjlist[point]:
                if nei not in visited:
                    heapq.heappush(minheap,[neicost,nei])
            
        return res

            
        
            
        

            











        


        



        
        