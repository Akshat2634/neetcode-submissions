class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        i = 0
        j = n-1
        mxArea = 0
        while i<j:
            ht = min(heights[i],heights[j])
            bd = j-i 
            area = ht * bd

            mxArea = max(mxArea,area)

            if heights[i]> heights[j]:
                j -=1
            else:
                i+=1
                
        return mxArea


        