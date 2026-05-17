class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        totalSize = 2 * length
        ans = [0] * totalSize


        for i in range(length):
            ans[i] = nums[i]
            ans[i+length] = nums[i]

        return ans 
