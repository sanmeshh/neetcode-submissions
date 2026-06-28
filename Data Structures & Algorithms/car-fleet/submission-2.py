class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        
        stack=[]

        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        
        cars.sort(reverse=True)
        n=len(cars)
        
        for p in range(n):
            stack.append((target-cars[p][0])/cars[p][1])

            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)
                
          








            

     

        

        


        


        