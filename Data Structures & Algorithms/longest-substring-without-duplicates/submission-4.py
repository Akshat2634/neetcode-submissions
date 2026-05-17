class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mxLen = 0
        n = len(s)

        for i in range(n):
            st = set()

            for j in range(i,n):
                if s[j] in st:
                    break
                st.add(s[j])
            mxLen = max(mxLen,len(st))

        return mxLen

