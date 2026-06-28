class Solution:
    def reverseBits(self, n: int) -> int:
        
        pos=[]
        for i in range(32):
            if n &(1<<i):
                pos.append(i)
        

        x=0
        for j in pos:
            x=(x|(1<<(31-j)))
        return x
            