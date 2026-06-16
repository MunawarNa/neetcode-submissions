class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = []
        for i in nums:
            if i not in numbers:
                numbers.append(i)
            else:
                return True
        return False
        



        
                         