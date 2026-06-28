class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices=[float('inf')]*n #dist of src to every node

        prices[src]=0#form src to src dist=0

        for i in range(k+1):
            tmpprices=prices.copy()#prices keeps on changing so instance

            for s,d,p in flights:
                if prices[s] ==float('inf'):
                    continue
                if prices[s]+p<tmpprices[d]:#if you find a better price for src to the des than update it
                #since we are in a sequence it will kinda add up to eg b tak jaane ka itna hai phir a se b se c tak jaane ka itna hoga
                    tmpprices[d]=prices[s]+p
            prices=tmpprices
        
        return -1 if prices[dst]==float('inf') else prices[dst]



        











        







        