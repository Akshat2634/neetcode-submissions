class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)
        uniq = set()
        for num in nums:
            if not num in uniq:
                uniq.add(num)
            else:
                return True
        return False
         