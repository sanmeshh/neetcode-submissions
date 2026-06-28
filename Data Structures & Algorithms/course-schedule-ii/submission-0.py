class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjlist={}
        for i in range(numCourses):#to fix keyerror with no list existing
            adjlist[i]=[]
        for crs,pre in prerequisites:
            adjlist[crs].append(pre)
    
        output=[]#the output
        visited,cycle=set(),set()
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True
            
            cycle.add(crs)#to detect ek given path,cycle hai ki nahi
            for pre in adjlist[crs]:
                if dfs(pre)==False:
                    return False
            
            cycle.remove(crs)#backtracking logic,for that path cycle set ka kaam hogya isiliye sab elements nikaal rahe hai

            visited.add(crs)#this course has been visited
            output.append(crs)#and added to the output set
            return True
        
        for c in range(numCourses):
            if dfs(c)==False:#each node pe dfs for topological sort
                return []
            
        return output 


        

        













        
        