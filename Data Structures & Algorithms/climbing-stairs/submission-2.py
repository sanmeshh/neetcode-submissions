class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1] * n
        def dfs(i):
            if i >= n:
                if i==n:
                    return 1
                else:
                    return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)#i+1,+2 refers to the choice we make
            #if that choice leads to 1 we made the right choice else it lead to 0
            #Also we are adding the number of  paths taken
            #if the path lead to 1 then it is added to the dp array if 0 then obv not added
            return cache[i]
        
        return dfs(0) 


        