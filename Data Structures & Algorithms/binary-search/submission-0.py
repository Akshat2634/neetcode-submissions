class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        e = len(nums)-1

        while(st<=e):
            mid = st + e-st//2   

            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                st = mid+1
            else:
                e = mid-1
            
        return -1

        