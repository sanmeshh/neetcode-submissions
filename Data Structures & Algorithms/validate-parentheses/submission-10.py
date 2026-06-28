class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeopen={ ")" : "(", "]" : "[", "}" : "{" }

        

        for c in s:
            if c in closeopen:
                if stack and closeopen[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
                
               
        return True if not stack else False
                    

        
        