class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        n = len(s)

        for i in range(n):
            st = set()
            for j in range(i,n):
                if s[j] in st:
                    break
                st.add(s[j])
            maxLen = max(maxLen,len(st))
    
        return maxLen
        