class Solution:

    def encode(self, strs: List[str]) -> str:
        self.ans=""
        for i in strs:
            self.ans=self.ans+i+'%01'

        return self.ans



        


    def decode(self, s: str) -> List[str]:
        if self.ans:
            self.ans=self.ans.split('%01')
            self.ans.pop(-1)
        else:
            return []
        return self.ans

