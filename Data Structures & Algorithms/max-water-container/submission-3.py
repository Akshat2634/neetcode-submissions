class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxAr = 0
        n = len(heights)

        i = 0 
        j = n-1

        while(i<j):
            ht = min(heights[i],heights[j])
            lt = j-i

            area = lt*ht

            maxAr = max(maxAr,area)
            
            if(heights[j]>heights[i]):
                i+=1

            else:
                j-=1
        
        return maxAr
        