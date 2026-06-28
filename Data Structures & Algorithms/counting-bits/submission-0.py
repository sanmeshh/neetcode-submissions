class Solution:
    def countBits(self, n: int) -> List[int]:

        res=[]
        for i in range(n+1):
            res.append(bin(i))
        
        for j in range(n+1):
            res[j]=res[j].count('1')
        return res
    


        