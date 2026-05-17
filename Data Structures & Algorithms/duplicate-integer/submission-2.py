class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = set()

        for num in nums:
            if not num in st:
                st.add(num)
            else:
                return True
        return False

         