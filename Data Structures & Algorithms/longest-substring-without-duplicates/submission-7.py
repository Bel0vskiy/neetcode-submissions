class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        seen = set()
        m = 0
        cnt = 0
        l = 0
        r = 0
        while(r<len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                cnt+=1
                m = max(m, cnt)
                r+=1
            else:
                while(s[r] in seen):
                    seen.remove(s[l])
                    l+=1
                    cnt-=1
        return m