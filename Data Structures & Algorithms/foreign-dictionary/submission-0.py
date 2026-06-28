class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj={c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen] == w2[:minlen]:
                return ""#this means the larger word is pehle than the smaller word which does not make sense

            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
# --- Start of Topological Sort ---

        visited={}
        ans=[]
        def dfs(c):
            if c in visited:
                return visited[c]# Returns True for a cycle, False if already fully visited
            
            visited[c]=True
        
            for nei in adj[c]:
                if dfs(nei):
                    return True #cycle detected
                
            visited[c]=False #path completed

            ans.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        ans.reverse()

        return "".join(ans)

# --- End of Topological Sort ---
        
"""
Not in visited: Never explored.

visited[char] = True: Currently on our recursion path (we're "visiting" it). If we encounter a character in this state, it means we've looped back on ourselves—we've found a cycle! 🔄

visited[char] = False: We have finished exploring this character and all characters that depend on it.
"""

            

        



        




        