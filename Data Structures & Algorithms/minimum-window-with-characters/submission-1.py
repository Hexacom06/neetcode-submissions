class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if t == "" or len(s) < len(t): return res
        hm, window = {}, {}
        for c in t:
            hm[c] = hm.get(c,0) + 1
        have, need = 0, len(hm)
        minss, l,  = 1010, 0
        for r in range(0,len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in hm and hm[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if minss > r - l + 1:
                    res = s[l:r+1]
                    minss = r-l+1
                window[s[l]] -= 1
                if s[l] in hm and hm[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        return res
            

            

