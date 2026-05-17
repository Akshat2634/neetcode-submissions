class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxArea=0
        while(left<right):
            ht = min(height[left], height[right])
            length = right-left
            area = ht*length
            maxArea = max(maxArea,area)
        
            if(height[right]>height[left]):
                left+=1

            else:
                right-=1
        return maxArea
        
        