class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap=Counter(tasks)
        maxheap=[-i for i in hmap.values()]
        #here maxheap is used for easy insertion and deletion
        heapq.heapify(maxheap)
        time=0
        q=deque()#for popleft

        while maxheap or q:
            time+=1
            if not maxheap:
                time=q[0][1]
            else:
                count=1+heapq.heappop(maxheap)#since one element is scheduled
                if count:
                    q.append([count,time+n])#after how much time do we have to schedule the same task
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time


        