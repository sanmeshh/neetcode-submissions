class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m=len(s)
        n=len(p)

        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            dp[i][0]=False


        
        for j in range(1,n+1):
            dp[0][j]=False

        dp[0][0]=True

        #if we have strings like a* , a*b* ,a*b*c*
        for j in range(2,n+1):
            if p[j-1]=='*':#                               a * b *
                dp[0][j]=dp[0][j-2]#str=a*b* then dp[0]=[T,F,T,F,T]

        #there are three cases here 

        for i in range(1,m+1):#we have extra padded row and column there 1->m
            for j in range(1,n+1):
                if p[j-1]=='.' or p[j-1]==s[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-2]#since * is '0' or more of the preceeding elem
                    #therefore we check if that pattern without (* and the element)
                    #is true or not
                    if p[j-2]=='.' or p[j-2]==s[i-1]:
                #that is false(if true then we have used 'or' below to save it)
                #
                        dp[i][j]=(dp[i][j] or dp[i-1][j])
                else:
                    dp[i][j]=False

        print(dp)
        
        return dp[-1][-1]




        
        
        






        

        

        


        