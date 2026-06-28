"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap=[]

        for interval in intervals:

            if min_heap and min_heap[0]<=interval.start:
                heapq.heappop(min_heap)#we just keep the number rooms in the heap
                #and those rooms are represented by the new_minimum end val of the room stored in the heap
                #now you'll ask why not maintain just a pointer , but we wont be able to to implement the 
                #count of the rooms ,thats why heap
            heapq.heappush(min_heap,interval.end)
        
        return len(min_heap)



        

            
                
            

                
    

        
        


        
        