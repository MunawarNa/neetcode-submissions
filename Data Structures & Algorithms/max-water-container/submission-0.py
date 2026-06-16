class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            height = min(heights[left],heights[right])
            width = right - left
            current_max = height * width
            if current_max > max_water:
                max_water = current_max
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_water


        