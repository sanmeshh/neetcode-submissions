from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for word in strs:
            key=sorted(word)
            key="".join(key)
            group[key].append(word)
        
        ans_list=list(group.values())

        return ans_list

        