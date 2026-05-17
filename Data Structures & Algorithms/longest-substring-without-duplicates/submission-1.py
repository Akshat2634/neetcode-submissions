class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mxlen = 0
        n = len(s)

        for i in range(n):
            st = set()
            for j in range(i,n):
                if s[j]in st:
                    break
                st.add(s[j])
            mxlen = max(mxlen,len(st))
        return mxlen