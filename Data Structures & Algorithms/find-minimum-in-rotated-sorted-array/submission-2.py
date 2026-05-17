class Solution:
    def findMin(self, nums: List[int]) -> int:

        st = 0
        e = len(nums)-1

        while st<e:
            mid = st + (e-st)//2 
            if(nums[mid]>nums[e]):
                st=mid+1
            else:
                e=mid
        return nums[st]
        