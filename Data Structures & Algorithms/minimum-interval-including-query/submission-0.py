class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        res={}
        i=0
        minheap=[]
        for q in sorted(queries):
            while i<len(intervals) and  intervals[i][0]<=q:#check if query lies in the interval or not
                l,r=intervals[i]
                heapq.heappush(minheap,(r-l+1,r))#r with len of interval is tie breaker if 
                #for near intervals where accept the first interval in the number line

                i+=1#we do not reset i to 0 since our queries are sorted and we dont want to loop over same intervals again

            while minheap and minheap[0][1]<q:#since we dont reset i we have to remove the unecessary intervals with small len but our query does not lie in it
                heapq.heappop(minheap)

            res[q]=minheap[0][0] if minheap else -1#if no soln then we return one
        return [res[q] for q in queries]#we use our hashmap to return the answer for each query

        
        



        





        
        