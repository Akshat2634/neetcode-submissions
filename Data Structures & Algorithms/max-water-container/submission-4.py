class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        i = 0 
        j = n-1
        maxArea = 0

        while(i<j):
            ht = min(heights[i], heights[j])
            breadth = j-i
            
            area = ht * breadth
            maxArea = max(maxArea,area)  

            if(heights[j]>heights[i]):
                i+=1

            else:
                j-=1
        return maxArea 