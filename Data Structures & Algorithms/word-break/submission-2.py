class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp=[False]*(len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                    #if agar apna word if equal nhi hai curr subtring k toh
                    #kya faydna na
                if i+len(w)<=len(s) and w==s[i:i+len(w)]:
                    dp[i]=dp[i+len(w)]
                    print(w,i)
                if dp[i]:
                    break
                #agar already true hai toh naye seq k liye nhi dekhna chahiye kyuki dusra false de skta
                #nhi samjha tu condition nikaal ke dekh aur run kar 
        print(dp)


        return dp[0]


        