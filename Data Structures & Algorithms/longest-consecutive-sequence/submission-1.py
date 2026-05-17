class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        maxlen = 0

        for num in nums:
            if num-1 not in num_set:
                currLen = 1
                curr = num

                while curr+1 in num_set:
                    currLen+=1
                    curr+=1
                
                maxlen = max(maxlen,currLen)
        return maxlen