class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        longest = 0

        # nums = [2,20,4,10,3,4,5]

        for num in nums_set:

            if num - 1 not in nums_set:
                current = num
                current_streak = 1

                while current + 1 in nums_set:
                    current += 1
                    current_streak += 1
                longest = max(longest, current_streak)
        return longest

            
            
                