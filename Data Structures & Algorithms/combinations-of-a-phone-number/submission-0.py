class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        chars={'2':'abc','3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=[]
        combs=[]
        n=len(digits)
        def dfs(i):
            if i==n-1:
                copy="".join(combs)
                ans.append(copy)
                return
            x=chars[digits[i+1]]
            for j in range(len(x)):
                combs.append(x[j])
                dfs(i+1)
                combs.pop()
        if n==0:
            return ans
        y=chars[digits[0]]
            
        for k in range(len(y)):
            combs.append(y[k])
            dfs(0)
            combs.pop()
        return ans

                
            


