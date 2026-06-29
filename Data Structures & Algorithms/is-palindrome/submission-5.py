class Solution:
    def isPalindrome(self, s: str) -> bool:

        text=re.sub(r"[^a-zA-Z0-9]", "", s)
    
        text=text.lower()
        if text==text[::-1]:
            return True 
        else:
            return False


        