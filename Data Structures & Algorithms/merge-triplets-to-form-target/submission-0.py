class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        f1,f2,f3=0,0,0
        for i in range(len(triplets)):

            if triplets[i][0]>target[0] or triplets[i][1]>target[1] or triplets[i][2]>target[2]:
                continue

            #since we can perform the operation zero or more times
            if triplets[i][0]==target[0]:
                f1=1
            
            if triplets[i][1]==target[1]:
                f2=1
            
            if triplets[i][2]==target[2]:
                f3=1
            
            if f1==f2==f3==1:
                return True
        return False
            

            
            


            

    






        
        