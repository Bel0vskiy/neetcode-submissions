class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        prev, curr = 1, 1
        for i in range(2, len(s)+1):
            next_val = 0
            if s[i-1] != '0':
                next_val+=curr
            tdig = int(s[i-2:i])
            if 10 <= tdig <= 26:
                next_val+=prev
            prev = curr
            curr = next_val
            if curr == 0:
                return 0
        return curr
