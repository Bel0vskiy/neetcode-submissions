class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            l,r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                cnt+=1
                l-=1
                r+=1
            l,r = i, i+1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                cnt+=1
                l-=1
                r+=1
        return cnt