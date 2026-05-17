class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        mxLen = 0

        for num in nums:
            if num-1 not in nums:
                curr = num
                length = 1

                while curr+1 in nums:
                    curr+=1
                    length+=1

                mxLen = max(mxLen,length)
        return mxLen