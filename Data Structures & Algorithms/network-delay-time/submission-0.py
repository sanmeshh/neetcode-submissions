class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i+1:[] for i in range(n)}
        for u, v, w in times:#make an adjlist
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:#this is 'q'
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                #if nhi visited hai toh hi run other wise inf loop
                continue
            visit.add(n1)
            t = max(t,w1)

            for n2, w2 in edges[n1]:#bfs logic
                    
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
        
        









        







        