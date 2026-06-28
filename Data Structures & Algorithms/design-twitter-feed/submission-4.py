class Twitter:

    def __init__(self):
        self.count=0
        self.followmap=defaultdict(set)
        self.tweetmap=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])#the time(count) at which it was tweeted        
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans=[]
        minheap=[]

        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:

                index=len(self.tweetmap[followeeId])-1
                count,tweetId=self.tweetmap[followeeId][index]
                heapq.heappush(minheap,[count,tweetId,followeeId,index-1])
      
        while minheap and len(ans)<10:
            count,tweetId,followeeId,index=heapq.heappop(minheap)
            ans.append(tweetId)#recent id
            if index>=0:
                count,tweetId=self.tweetmap[followeeId][index]
                heapq.heappush(minheap,[count,tweetId,followeeId,index-1])#next tweet from the same followeeId
        return ans
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
