class Solution:
    def longestPalindrome(self, s: str) -> str:

        #actually 2d problem
        n=len(s)
        dp=[[False]*n for _ in range(n)]

        idx=0
        reslen=0


        for i in range(n):
            for j in range(i+1):

                if s[j]==s[i] and (i-j<=2 or dp[j+1][i-1]):

                    dp[j][i]=True
                    if reslen<(i-j+1):
                        idx=j
                        reslen=(i-j+1)
        
        return s[idx:idx+reslen]
        













       

            




        
        