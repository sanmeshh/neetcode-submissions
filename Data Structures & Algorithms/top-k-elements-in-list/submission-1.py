class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        check=set(nums)
        hashmap={}
        
        for num in check:
            hashmap[num]=0
        
        for num in nums:
            hashmap[num]+=1

        
        dic=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)

        dic=dic[:k]
        ans=[]
        for i in dic:
            ans.append(i[0])

        return ans
    
        
        

        
