class Solution:
    def findMin(self, nums: List[int]) -> int:
        stack = []

        for i in nums:
            if not stack or i < stack[-1]:
                stack.append(i)
            
        return stack[-1]

        