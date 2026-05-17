class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_mp = {}

        for i , num in enumerate(nums):
            rem = target - num
            if rem in num_mp:
                return [num_mp[rem],i]
            num_mp[num] = i
            
        