class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_mp = {}

        for i, num in enumerate(nums):
            remain = target - num
            if remain in num_mp:
                return[num_mp[remain],i]
            num_mp[num] = i
        
            
        