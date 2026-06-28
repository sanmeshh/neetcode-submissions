class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(s)<len(t):
            return 0
        cache={}
        def dfs(i,j):

            if j==len(t):#for empty t ,theres only 1 subsq
                return 1
            
            if i==len(s):#if t is not empty but s is,
                return 0

            if (i,j) in cache:
                return  cache[(i,j)]
            
            if s[i]==t[j]:
                #either we take the curr element in s or the next element
                cache[(i,j)]=dfs(i+1,j+1)+dfs(i+1,j)
            else:
                cache[(i,j)]=dfs(i+1,j)#we just skip it here
            
            return cache[(i,j)]

        return dfs(0,0)
            


            


        
        