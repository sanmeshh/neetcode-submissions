class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i,arr in enumerate(matrix):
         
            if target<=arr[-1]:
                break

        low=0
        high=len(matrix[0])-1
        arr=matrix[i]
        while low<=high:
            mid=int((low+high)/2)

            if arr[mid]==target:
                return True
            
            elif arr[mid]<target:
                low=mid+1
            
            else:

                high=mid-1
        return False

        