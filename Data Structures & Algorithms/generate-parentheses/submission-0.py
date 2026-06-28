class Solution:
    def generateParenthesis(self, n: int):

        stack=[]
        ans=[]


        def backtrack(openb,closedb):

            if openb==closedb==n:
                ans.append("".join(stack))
                return
            
            if openb<n:
                stack.append("(")
                backtrack(openb+1,closedb)
                stack.pop()
                # it removes the last added parenthesis to explore other possibilities
                #after backtrack(x,y) returns a combination in the global value in stack

            if closedb<openb:
                stack.append(")")
                backtrack(openb,closedb+1)
                stack.pop()


        backtrack(0,0)
        
        return ans
                
                

                


            


        








        





        
        