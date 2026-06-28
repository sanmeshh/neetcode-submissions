class Solution:
    def search(self, arr : List[int], target: int) -> int:

        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<arr[high]:
                high=mid
            elif arr[mid]>arr[high]:
                low=mid+1
            else:
                break
        high=len(arr)-1
        if target>arr[high]:
                high=low-1
                low=0
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>target:
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            else:
                return mid
        return -1



                











        