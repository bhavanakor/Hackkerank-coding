class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum=0
        left=0
        right=len(height)-1
        while left<right:
            hold=min(height[left],height[right])
            area=hold*(right-left)
            if area>maximum:
                maximum=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maximum
