class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t=="":return ""
        #counts occurences in t,counts occurences in our output window
        hmap,window={},{}

        for c in t:
            hmap[c]=1+hmap.get(c,0)

        have,need=0,len(hmap)
        res=[-1,-1]#returns the l and  r pointer
        reslen=float('inf')

        l=0
        for r in range(len(s)):
            c=s[r]

            window[c]=1+window.get(c,0)
            if c in hmap and window[c]==hmap[c]:
                have+=1

            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1

                #shrinking the window count from left 
                window[s[l]]-=1
                if s[l] in hmap and window[s[l]]< hmap[s[l]]:
                    have-=1
                l+=1
        l,r=res

        return s[l:r+1] if reslen!=float('inf') else ""       